<p align="center">
 <img src="https://i.imgur.com/rSyq3MW.png" alt="The Documentation Compendium"></a>
</p>

<h3 align="center">Major Research Paper: “Compartimental SIR model applied to Covid-19 pandemic”</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-inactive-red.svg)]()
  [![RepoSize](https://img.shields.io/github/repo-size/pythonjul/major-research-paper)]()

</div>

---

<p align = "center">💡 In 2020-21, I have analysed different Covid-19 model</p>



## Why I made this project? <a name = "why_document"></a>

- It was my Research Paper to validate my master degree.

## Introduction<a name = "how_to_play"></a>
- How do the models used on the Covid-19 epidemic work? We started this work in February 2020. And it was during this same period that Covid-19 was spreading widely in populations around the world. When Professor José Rolim proposed that we work on this subject after reading the last chapters of the book Networks, Crowds, and Markets, I immediately said yes with enthusiasm, as the subject was so fascinating and topical.

- At the beginning of 2020, we didn't know how our lives would be so impacted afterwards. Scientists all over the world were studying Covid-19 to better understand it. As a result, modelling improved with the knowledge gained about how the virus behaves.

- We will try to understand how an epidemiological model called the SIR model works. This model is regularly used in Covid-19 modelling. 

- How does it behave? What can it achieve? What are its limitations? We will develop each of these questions in the rest of this work.

## How to use the functions? ##
- If you're only interested in the results, download the pdf file. Otherwise, download also the other files.

<dl>
  <dt>Procedure_1</dt>
  <dd>Purpose: to calculate the beta sigma gamma S_0 E_0 parameters with P1 for a given country.</dd>
  <dd>in: table of infections received, (pathfile to be changed for program execution), country, date range, population of the country, estimate of beta-sigma-gamma parameters. </dd>
  <dd>out: return beta sigma gamma parameters for procedure 1.</dd>
</dl>


<dl>
  <dt>Procedure_2-3</dt>
  <dd>Purpose: to calculate the beta sigma gamma parameters S_0 E_0 with P2 and P3 for a given country.</dd>
  <dd>in: table of recent infections, table of estimated infections, (pathfile ` change for program execution), country, method (IHME,YGG,ICL,LSHTM), date range, population of the country, estimation of beta-sigma-gamma parameters.</dd>
  <dd>out: return beta sigma gamma parameters S_0 E_0 for procedure 2 and procedure 3.</dd>
</dl>


<dl>
  <dt>Procedure_3_affichage</dt>
  <dd>Purpose: display the 4 methods and the confirmed cases for a given country.</dd>
  <dd>in: table of confirmed infections, table of simulated infections (pathfile to be changed for program execution), country, date range.</dd>
  <dd>  out: returns the complete graph as well as a zoomed graph on a given period.</dd>
</dl>


<dl>
  <dt>Procedure_3_monde</dt>
  <dd>Purpose: to calculate the beta sigma gamma S_0 E_0 parameters with P3 for all countries in the world.</dd>
  <dd>  in: table of estimated infections, (pathfile ` change for program execution), method (IHME,YGG,ICL,LSHTM), date range, estimate of beta-sigma-gamma parameters.</dd>
  <dd>  out: returns the beta sigma gamma parameters S_0 E_0 for procedure 3.</dd>
</dl>


<dl>
  <dt>SEIR_model</dt>
  <dd>Purpose: to display a SEIR model.</dd>
  <dd>in: N, R0, E0, I0, S0, beta, gamma: parameters of the SIR model, T: the desired time interval.</dd>
  <dd>out: the values of the functions S, E, I and R and the corresponding SEIR graph.</dd>
</dl>

<dl>
  <dt>SIR_model</dt>
  <dd>Purpose: to display a SIR model.</dd>
  <dd>in: N, R0, I0, S0, beta, gamma: parameters of the SIR model, T: the desired time interval.</dd>
  <dd>out: the values of the functions S, I and R and the corresponding SIR graph.</dd>
</dl>

<dl>
  <dt>Cas_estimes_recenses_monde</dt>
  <dd>Purpose: to display the data (4 methods + confirmed cases) for the world.</dd>
  <dd>in: table of data for the world.</dd>
  <dd>out: graph.</dd>
</dl>

<dl>
  <dt>beta_petit_puis_grand</dt>
  <dd>Purpose: to create a graph with a beta value that changes over time.</dd>
  <dd>in: beta value, gamma, and initial conditions.</dd>
  <dd>out: two graphs concatenated together.</dd>
</dl>

## Built With ##

- Python
- R

## Author

**Julien Python**

- [Profile](https://github.com/pythonjul "Julien Python")
- [Email](mailto:pythonjul@gmail.com?subject=Hello "Hello!")
