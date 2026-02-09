import sagemaker
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import TrainingStep
from sagemaker.workflow.clarify_check_step import ClarifyCheckStep, DataConfig, BiasConfig
from sagemaker.model_monitor import DatasetFormat

# 1. SETUP - Defining the "Protected Attribute" (e.g., Gender or Age)
# In EU AI Act terms, this is checking for "Prohibited Discrimination"
facet_name = "gender"  # The attribute we are checking for bias
target_name = "loan_approved" # The model's prediction

# 2. DATA CONFIG - Where the validation data sits in S3
data_config = DataConfig(
    s3_data_input_path="s3://your-actready-bucket/validation-data.csv",
    s3_output_path="s3://your-actready-bucket/clarify-results/",
    label=target_name,
    dataset_type=DatasetFormat.CSV
)

# 3. BIAS CONFIG - Defining what "Fairness" looks like
bias_config = BiasConfig(
    label_values_or_threshold=[1], # 1 = Loan Approved
    facet_name=facet_name,
    facet_values_or_threshold=[0] # Checking if group '0' is treated unfairly
)

# 4. THE CLARIFY CHECK STEP (The "Compliance Guardrail")
# This is the 'ActReady' heart of the pipeline
bias_check_step = ClarifyCheckStep(
    name="ActReady-Bias-Audit",
    clarify_check_config=sagemaker.workflow.clarify_check_step.ClarifyCheckConfig(
        data_config=data_config,
        bias_config=bias_config
    ),
    check_job_config=sagemaker.workflow.steps.CheckJobConfig(
        role="arn:aws:iam::your-account-id:role/ActReady-Compliance-Role",
        instance_type="ml.m5.xlarge",
        volume_size_in_gb=20
    ),
    skip_check=False, # Mandatory for Compliance
    register_new_baseline=True
)

# 5. CREATE THE PIPELINE
pipeline = Pipeline(
    name="ActReady-Compliance-Pipeline",
    steps=[bias_check_step] # In a full project, you'd add TrainingStep before this
)
