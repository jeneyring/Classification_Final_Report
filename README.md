# Classification_Final_Report

### <b>Project Description:</b><br>
This is my final project to find the lead drivers for customer churn at Telco. 

<b>In this project I will explore and Hypothesis test the Telco dataset to find any relations between different Telco customer demographics and churn.

I then will construct a ML classification model that can accurately predict Telco's customer churn.</b>


Included in the Final Report file, there is Scratchpad file with the step-by-step process of the key findings of how the key driver(s) were found, the models and their accuracy used in creating the ML model and what the outcomes vs. my initial hypothesis were.

### <b>Project Goals:</b><br>
To find the demographic drivers of Telco's high churn rate and their subgroups (or 'why' of churning).


### <b>Deliverables:</b><br>
- A classification model that will use the found driver(s) to predict Telco's churn rate with 80% accuracy of whether a group of customers will churn or not.
- A final notebook presentation.
- 5min presentation and breakdown of the final process.

### <b>Data Dictionary:</b><br>
|Target|Datatype|Definition|
|:-------|:--------|:----------|
| churn | 7043 non-null: object | Telco's recent customer churn list |

|Feature|Datatype|Definition|
|:-------|:--------|:----------|
| gender           |  7043 non-null: object | gender of Telco customers|
| senior_citizen   |  7043 non-null: int64  | 60+ aged Telco customers|
| partner          |  7043 non-null: object | Telco customers with/without partner|
| dependents       |  7043 non-null: object | Customers with/without dependents|
| contract_type    |  7043 non-null: object | Contract types for customers|
| internet_service_type |  7043 non-null: object | None; DSL; Fiber Optic types|
| payment_types    |  7043 non-null: object | payment forms for Customers|



 ### <b>Initial Hypothesis and Questions:</b><br>

#### Hypothesis 1 
> - alpha = 0.05
> - H0: There is NO relationship between churn and customers without partners
> - Ha: There IS a relationship between churn and customers without partners
> - <b>Outcome: I rejected the Null Hypothesis, in that there is a relationship with single customers and churn.</b>

#### Hypothesis 2 
> - alpha = 0.05
> - H0: There is NO relationship between churn and customers with dependents
> - Ha: There IS a relationship between churn and customers with dependents
> - <b>Outcome: I rejected the Null Hypothesis, in that there is a relationship with customers that have dependents and the high churn rate.</b>

<hr style="border-top: 10px green; margin-top: 1px; margin-bottom: 1px"></hr>


 ### <b>Project Planning (aka How I think I'll get there!):</b><br>
 <b>STEPS AHEAD:</b><br>
 - Explore these 3 churn drivers
     (ie. charts, crosstabs, hypothesis testing)
 - Create classification models to train, validate, and test drivers on



 <b>MY PROJECT CHECK-LIST:</b><br>
 - Create acquire and prepare.py modules
 - Log down process and questions/takeaways along the way
 - Construct ML models


 - <b> FINAL REPORT: </b><br>
    - use markdown to guide audience
      - (all cells with code need comments!)
    - Begin project with Overview and Goals
    - End project with a Conclusion (how relates to beginning goals)
    - Exploration portion only has charts/data that is important
    - Include 4 visualizations: Question | Visualization | Statistical Test (at least 2 | 
             - <i> must</i> provide markdown for these visuals
    - Provide context of target variable to visualization parameters
    - Include 3 best models 
         - Show steps and code to fit/evaluate/ and select those models
    -On best model, chart visually how it performed on its test
