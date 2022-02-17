rm(list=ls())
library(ggplot2)
library(pomp)
library(sqldf)

'
But: calculer les paramètres beta sigma gamma S_0 E_0 avec P3 pour tous les pays du monde.

  in: tableau des infections estimées, (pathfile à changer pour exécution du programme)
      méthode (IHME,YGG,ICL,LSHTM), intervalle de dates, 
      estimation des paramètres beta-sigma-gamma
  out:retourne les paramètres beta sigma gamma S_0 E_0 pour la procédure 3
'

#c1-pays c2-code c3-date c4-ICL c5-IHME c6-YGG c7-LSHTM c8-confirmed_cases
ma_fct_monde<-function(methode_DM,line_begin,line_end){
  tab0 <- read.csv("these/death_model/daily-new-estimated-infections-of-covid-19.csv")
  colnames(tab0) <- c("pays","code","dates","ICL","IHME","YGG","LSHTM","confirmed_cases")
  
  tab01<-sqldf('SELECT * FROM tab0 WHERE pays NOT LIKE "World%"') #sans le world
  
  tab_world<-sqldf('SELECT dates,SUM(ICL) AS ICL, SUM(IHME) AS IHME,SUM(YGG) AS YGG,SUM(LSHTM) AS LSHTM FROM tab01 GROUP BY dates')
  write.csv(df,"these/death_model/my_tab_world.csv", row.names = FALSE) #ce fichier est utilisé pour le code Cas_estimes_recenses_monde
  
  tab1 <- subset(tab_world, select = c("dates",methode_DM))
  
  tab2 <- tab1[line_begin:line_end,2]
  tab_df<-data.frame("dates"=1:length(tab2),methode_DM=tab2)
  
  pomp(
    data=tab_df,
    times=1:length(tab2),
    t0=0,
    skeleton=vectorfield(
      Csnippet("
        DS = -Beta*I*S/N;
        DE = Beta*I*S/N-sigma*E;
        DI = sigma*E-gamma*I;
        DR = gamma*I;")),
    rinit=Csnippet("
        S = S_0;
        E = E_0;
        I = I_0;
        R = N-S_0-E_0-I_0;"),
    statenames=c("S","E","I","R"),
    paramnames=c("Beta","sigma","gamma","N","S_0","E_0","I_0")) -> niameyA_c
  
  sse <- function (params) {
    x <- trajectory(niameyA_c,params=params)
    discrep <- x["I",,]-obs(niameyA_c)
    sum(discrep^2)
  }
  
  popul=7.9e+10; #world
  
  f2 <- function (par) {
    params <- c(Beta=par[1],sigma=par[2],gamma=par[3],N=popul,S_0=par[4],E_0=par[5],I_0=tab2[1]) # beta sigma gamma S0 E0
    sse(params)
  }
  borne_inf=c(0.1,0.07,0.05,0,0)*0.8
  borne_sup=c(0.3,0.5,0.1,popul,popul)*1.2
  optim(fn=f2,par=c(0.2,0.2,0.08,popul-tab2[1]-((tab2[1]+tab2[2])/2),(tab2[1]+tab2[2])/2),lower = -Inf, upper = Inf,method="L-BFGS-B") -> fit2
  cat(paste("\n","pour (aucune borne)",methode_DM,"on obtient----------------------:"))
  cat("\n",fit2$par,"\n")
  optim(fn=f2,par=c(0.2,0.2,0.08,popul-tab2[1]-((tab2[1]+tab2[2])/2),(tab2[1]+tab2[2])/2),lower = 0.001, upper = Inf,method="L-BFGS-B") -> fit2
  cat(paste("\n","pour (borne positive)",methode_DM,"on obtient--------------------:"))
  cat("\n",fit2$par)
  optim(fn=f2,par=c(0.2,0.2,0.08,popul-tab2[1]-((tab2[1]+tab2[2])/2),(tab2[1]+tab2[2])/2),lower = borne_inf, upper = borne_sup,method="L-BFGS-B") -> fit2
  cat(paste("\n","pour (borne interv)",methode_DM,"on obtient----------------------:"))
  cat("\n",fit2$par,"\n")
}

for (m in c("ICL","IHME","YGG","LSHTM")){ma_fct_monde(methode_DM =m,94,129)}#2020-03-01 au 2020-04-05