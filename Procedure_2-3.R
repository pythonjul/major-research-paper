rm(list=ls())
library(ggplot2)
library(pomp)

'
But: calculer les paramètres beta sigma gamma S_0 E_0 avec P2 et P3 pour un pays donné.

  in: tableau des infections recencées, tableau des infections estimées, (pathfile à changer pour exécution du programme)
      pays, méthode (IHME,YGG,ICL,LSHTM), intervalle de dates, 
      population du pays, estimation des paramètres beta-sigma-gamma
  out:retourne les paramètres beta sigma gamma S_0 E_0 pour la procédure 2 et la procédure 3
'
# Insérer input souhaités
pays_sel<-"United States"
methode_DM2<-"new_cases_smoothed"
methode_DM<-"IHME"
d1<-"2020-02-09"
d2<-"2020-02-29"

tab00 <- read.csv("these/en_autrespays_maj/owid-covid-data.csv")
tab11 <- subset(tab00, location==pays_sel,select = c(date,new_cases_smoothed))

start_date2<-match(d1,tab11$date)
end_date2<-match(d2,tab11$date)

popul=230000000; #United States
# popul=8600000; #Switzerland
# popul=67422000; #France
# popul=11600000; #Belgium
# popul=10700000; #Czchia
# popul=8700000; #Israel
# popul=1380000000; #India

tab22 <- tab11[start_date2:end_date2,2]
tab_df2<-data.frame("dates"=1:length(tab22),methode_DM2=tab22)

pomp(
  data=tab_df2,
  times=1:length(tab22),
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
  paramnames=c("Beta","sigma","gamma","N","S_0","E_0","I_0")) -> niameyA

sse2 <- function (params) {
  x <- trajectory(niameyA,params=params)
  discrep <- x["I",,]-obs(niameyA)
  sum(discrep^2)
}

f22 <- function (par) {
  params <- c(Beta=par[1],sigma=par[2],gamma=par[3],N=popul,S_0=par[4],E_0=par[5],I_0=tab22[1]) # beta sigma gamma S0 E0
  sse2(params)
}

optim(fn=f22,par=c(0.2,0.2,0.08,popul-tab22[1]-((tab22[1]+tab22[2])/2),(tab22[1]+tab22[2])/2),lower = 0.001, upper = Inf,method="L-BFGS-B") -> fit22


tab0 <- read.csv("these/death_model/daily-new-estimated-infections-of-covid-19.csv")
colnames(tab0) <- c("pays","code","dates","ICL","IHME","YGG","LSHTM","confirmed_cases")
tab1 <- subset(tab0, pays==pays_sel,select = c("dates",methode_DM))

start_date<-match(d1,tab1$dates)
end_date<-match(d2,tab1$dates)

tab2 <- tab1[start_date:end_date,2]
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

f2 <- function (par) {
  params <- c(Beta=par[1],sigma=par[2],gamma=par[3],N=popul,S_0=par[4],E_0=par[5],I_0=tab2[1]) # beta sigma gamma S0 E0
  sse(params)
}

optim(fn=f2,par=c(0.2,0.2,0.08,popul-tab2[1]-((tab2[1]+tab2[2])/2),(tab2[1]+tab2[2])/2),lower = 0.001, upper = Inf,method="L-BFGS-B") -> fit2

cat(paste("\n","pour P2",methode_DM2,pays_sel,"on obtient--------------------:"))
cat("\n",fit22$par,"\n")


cat(paste("\n","pour P3 (deathratio)",methode_DM,pays_sel,"on obtient--------:"))
cat("\n",fit2$par,"\n")
