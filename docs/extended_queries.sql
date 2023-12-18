select * from pathways;
select * from clingene;
select * from clinicaltrials;
select * from mydb.resultsclinicaltrials;
select * from articlespubmed;

insert into pathways_copy1 select * from pathways;
insert into resultsclinicaltrials_copy1 select * from resultsclinicaltrials;

-- SET FOREIGN_KEY_CHECKS=0;

-- Consulta Where 1
select Description from pathways where Subject = 'Metabolic' limit 150;
select Description from pathways_copy1 where Subject = 'Metabolic' limit 150;

-- Consulta Where 2
select Subject from pathways where Description like '%Citric%';
select Subject from pathways_copy1 where Description like '%Citric%';

-- Consulta Where 3
select count(Conditions) from clinicaltrials where Interventions = 'Drug: Perifosine|Drug: Capecitabine';
select count(Conditions) from clinicaltrials_copy1 where Interventions = 'Drug: Perifosine|Drug: Capecitabine';


-- Consulta Where + Inner Join 1
select Citation
from articlespubmed 
inner join resultsclinicaltrials 
on resultsclinicaltrials.idResultsClinicalTrial = articlespubmed.resultsclinicaltrials_idResultsClinicalTrials
where Study
like '%melanoma%';

select Citation
from articlespubmed_copy1
inner join resultsclinicaltrials_copy1 
on resultsclinicaltrials_copy1.idResultsClinicalTrial = articlespubmed_copy1.resultsclinicaltrials_idResultsClinicalTrials
where Study
like '%melanoma%';

-- Consulta Where + Inner Join 2
select Study
from resultsclinicaltrials 
inner join articlespubmed
on  resultsclinicaltrials.idResultsClinicalTrial = articlespubmed.resultsclinicaltrials_idResultsClinicalTrials
where Title
like '%Update%'
and Title
like '%Autoimmune%';

select Study
from resultsclinicaltrials_copy1 
inner join articlespubmed_copy1
on  resultsclinicaltrials_copy1.idResultsClinicalTrial = articlespubmed_copy1.resultsclinicaltrials_idResultsClinicalTrials
where Title
like '%Update%'
and Title
like '%Autoimmune%';

-- Consulta Where + Inner Join 3
select Name, Description, DiseaseLabel, GCEP
from pathways 
inner join clingene
on  pathways.idPathways = clingene.Pathways_idPathways1
where GCEP = 'Peroxisomal Disorders';

select Name, Description, DiseaseLabel, GCEP
from pathways_copy1 
inner join clingene_copy1
on  pathways_copy1.idPathways = clingene_copy1.Pathways_idPathways1
where GCEP = 'Peroxisomal Disorders';


-- Consulta Where + Subquery1
select Interventions 
from clinicaltrials 
where exists 
(select study 
from resultsclinicaltrials 
where resultsclinicaltrials.clinicaltrials_idClinicalTrials = clinicaltrials.idClinicalTrials 
and Study like '%cancer%');

select Interventions 
from clinicaltrials_copy1
where exists 
(select study 
from resultsclinicaltrials_copy1 
where resultsclinicaltrials_copy1.clinicaltrials_idClinicalTrials = clinicaltrials_copy1.idClinicalTrials 
and Study like '%cancer%');

-- Consulta Where + Subquery 2
select Title 
from articlespubmed 
where resultsclinicaltrials_clinicaltrials_idClinicalTrials in 
( select idClinicalTrials 
from clinicaltrials 
where Conditions = 'Colon Cancer' );

select Title 
from articlespubmed_copy1 
where resultsclinicaltrials_clinicaltrials_idClinicalTrials in 
( select idClinicalTrials
from clinicaltrials_copy1 
where Conditions = 'Colon Cancer' );

-- Consulta Where + Subquery 3
select DiseaseLabel 
from clingene 
where Pathways_idPathways1 in 
( select idPathways 
from pathways
where Subject = 'Disease' and Description like '%Bile Acid%');

select DiseaseLabel 
from clingene_copy1 
where Pathways_idPathways1 in 
( select idPathways 
from pathways_copy1
where Subject = 'Disease' and Description like '%Bile Acid%');

SELECT clingene.ClinGenecol2, clinicaltrials.ClinicalTrialscol3
FROM ((clingene_has_clinicaltrials
INNER JOIN clingene ON clingene.ClinGenecol = clingene_has_clinicaltrials.clingene_ClinGenecol)
INNER JOIN clinicaltrials ON clinicaltrials.idClinicalTrials = clingene_has_clinicaltrials. clinicaltrials_idClinicalTrials)
where ClinGenecol1 = 'long chain acyl-CoA dehydrogenase deficiency';


-- Consultas join Mongo
select *
from pathways 
inner join clingene
on  pathways.idPathways = clingene.Pathways_idPathways1;

SELECT *
FROM ((clingene_has_clinicaltrials
INNER JOIN clingene ON clingene.idClinGene = clingene_has_clinicaltrials.clingene_idClinGene)
INNER JOIN clinicaltrials ON clinicaltrials.idClinicalTrials = clingene_has_clinicaltrials. clinicaltrials_idClinicalTrials);

select *
from resultsclinicaltrials 
inner join articlespubmed
on  idResultsClinicalTrial = resultsclinicaltrials_idResultsClinicalTrials;

select *
from clinicaltrials 
inner join articlespubmed
on  idClinicalTrials = resultsclinicaltrials_clinicaltrials_idClinicalTrials;

select *
from clinicaltrials 
inner join resultsclinicaltrials
on  idClinicalTrials = clinicaltrials_idClinicalTrials;