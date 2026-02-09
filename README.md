# ⚖️ SageMaker Bias Detection Pipeline (EU AI Act Compliance)

This repository demonstrates an **Automated MLOps Pipeline** that integrates **Bias & Fairness Auditing** as a mandatory deployment gate.

### 🛡️ Why this matters for the EU AI Act
Under **Article 10 (Data and Data Governance)**, providers of High-Risk AI systems must implement "appropriate measures to detect, prevent and mitigate possible biases." 

This pipeline automates that requirement by:
1. **Auditing protected facets** (Age, Gender, etc.) during the training lifecycle.
2. **Generating Compliance Reports** automatically in S3.
3. **Failing the build** if bias metrics (like Disparate Impact) exceed legal thresholds.

### 🛠️ Technology
- **AWS SageMaker Clarify:** To calculate pre-training and post-training bias metrics.
- **SageMaker Pipelines:** For end-to-end automation.
- **Python SDK:** Implementation of `ClarifyCheckStep`.

**Built by Alaison | ActReady AI**
