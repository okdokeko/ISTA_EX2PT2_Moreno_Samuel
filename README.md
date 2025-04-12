# Exam 2, Portion 2 - Samuel Moreno
DISCLOSURE: No AI was used but a whole lot internet was, sources are detailed in the jupyter notebook.
Please look in the jupyter notebook to see the structured answers, it was super confusing trying to jump around all the files but here they are also for convenience:

# Exam 2, Portion 2 - Samuel Moreno

#### (5 points): If you are not familiar with this kind of scenario, but you were hired for this job in the real world, you would need to learn about it. Find two resources on the internet that are reliable and of good research quality (no forums, blogs, videos, social media, etc...)

Source 1: https://pmc.ncbi.nlm.nih.gov/articles/PMC4953449/

Key takeaways: Readmitted patientss are older on average, initial stay was longer for readmitted patient, an overwhelming majority of readmitted patients could have been avoided, readmission without conclusive therapy was the leading cause for readmission.

Source 2: https://pmc.ncbi.nlm.nih.gov/articles/PMC4953449/

Key takeaways: Around 20% of medicare beneficieares experience readmission within 30 days. Hospitals have been taken preventive measures to try to avoid readmissions being as frequent, and have reduced the percentage by about 5% over the years. 

"The most common preventable factors were emergency department decision-making regarding readmission, failure to relay important information to outpatient providers, discharge of patients too soon, and lack of goals of care discussions among patients with serious illnesses. "

#### (5 points): Download this dataset and assess it using ISLP 3.3 and 3.4 (like how you did for homework 3).

##### The 12 columns, what they are, and their data types are as follow:
1. Facility Name, the name of the hospital this patient was under study for, this is an object type (category since its just a string).
2. Facility ID is the ID of the hospital encoded to its name, the dtype is int64 but it should probably be treated as a categorical variable as well.
3. State; the state the hospital is in; object since its 2 letters.
4. Measure Name; I think this is the condition the data pertains to?; object since its strings.
5. Number of Discharges; # of discharges for the measure/condition; float64 since its a number.
6. Footnote; I think this is a reason for not including any of the following 4 columns; float64 since its a number. 
7. Excess Readmission Ratio; a ratio of expected readmissions > 1 is more than expected and vice versa for the condition, float64 since its a number.
8. Predicted Readmission Rate; predicted readmissions for the condition * the readmission rate for patient/condition. float64 since num.
9. Expected Readmission Rate; this is like the national avg for the condition or patient or smth like that. float64 since num.
10. Number of Readmissions; the num of readmissions for that condition, object since a lot of data points are "Too Few to Report"
11. Start Date; beginning of data collection, object since its structured date format.
12. End Date; end of data collection, object since its structured date format.

#### (5 points): Form your research question that can be answered by this dataset.
What factors impact the number of readmissions the most?
By extension: Which and how can these factors be manipulated to reduce the number of reradmissions.

#### (5 points): Explain why your research question would be interesting to the board-- do not tailor your research question to me just because I'm your machine learning instructor. I'm interested in your model, but the board cares about money/patients

The board most likely cares about saving money more than anything else, so if I taylor my question to help answer how to reduce readmissions this would be enticing for them. 

#### (40 points): Choose any algorithm from chapter 5, 6, 7, or 8 to answer your research question. Explain your choice.
    Write your algorithm from scratch.
    Include resources used for writing your algorithm. 
    If you choose to use generative AI-- and the gen AI model gets something wrong -- you will be docked for its mistakes. A mistake can include, but is not limited to: code mistakes, getting the right answer for the wrong reason, using a model for the wrong datatypes, ethical violations and assumptions made by the model, etc... 

A: I am going to be doing a stepwise forward selection to predict the number of readmissions for my model. This will kind of know out the bad features and also give coefficients for the more important features.

Here are my sources:

https://automaticaddison.com/stepwise-forward-selection-algorithm-from-scratch/

https://fakhredin.medium.com/forward-selection-to-find-predictive-variables-with-python-code-3c33f0db2393

https://en.wikipedia.org/wiki/Coefficient_of_determination

As shown, the coefficient of my models are pretty similar:

My model:
The values of B is: [ 0.15149975  0.45589187 -0.02384048]
The value of B_0 is:  -0.03843306681496902
R Squared is: 0.8135228933312568

SKLearn:
sklearn coefficient (B): [ 0.16794386  3.56523232 86.95667148]
sklearn intercept (B_0): -147.3791049396031
sklearn R-squared: 0.9197903563760922

The R squared values are very similar but the coefficients are quite different (especially the last).
I think I had to scale but everytime I tried everything broe so I ended up giving up on that.

#### (5 points): In a few sentences, tell the board your conclusions, predictions, and recommendations.
In conclusion, the most important factors are Number of Discharges, Predicted Readmission Rate, and Excess Readmission Ratio, all of which positively affect the amount of readmissions. Surprisingly, Expected Readmission Rate is not as impactful in the model. As such, I would recommend trying to reduce these ratios?