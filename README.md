# Claim Outcome Prediction — Assessment Kit

This is a structured starter kit, not a completed assessment. The assessment brief explicitly asks candidates not to have an AI tool generate the solution. Complete the TODOs yourself, run the project, understand the decisions, and enter only actual measured results.

## Deliverables
1. Generate 300–500 simulated claims with columns: id, payer, provider, cpt_code, diagnosis_code, billed_amount, patient_age, status.
2. Maintain approximately 70% Paid, 20% Partially_Paid, 10% Denied.
3. Use a stratified train/test split.
4. Engineer at least two features. Target-derived statistics must be fitted on training rows only.
5. Train a classifier and save the complete preprocessing + model pipeline.
6. Report per-class precision, recall, F1-score, and confusion matrix.
7. Explain the weakest class and one improvement.
8. Implement POST /predict with predicted status, probabilities, and input validation.

## Setup (Windows PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
If activation is blocked:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## Run after completing TODOs
```powershell
python data/generate_data.py
python train.py
uvicorn app:app --reload
```
Open http://127.0.0.1:8000/docs to test the API.

## API request format
```json
{
  "payer": "Aetna",
  "provider": "Dr. Rao",
  "cpt_code": "99213",
  "diagnosis_code": "M54.5",
  "billed_amount": 220.00,
  "patient_age": 45
}
```
Expected response shape (illustrative only; not measured output):
```json
{
  "predicted_status": "Paid",
  "probabilities": {
    "Paid": 0.81,
    "Partially_Paid": 0.14,
    "Denied": 0.05
  }
}
```

## Actual held-out evaluation results — fill after running
| Class | Precision | Recall | F1-score |
|---|---:|---:|---:|
| Paid | TODO | TODO | TODO |
| Partially_Paid | TODO | TODO | TODO |
| Denied | TODO | TODO | TODO |

Confusion matrix: TODO

Weakest class: TODO

One concrete improvement: TODO

## Assumptions and limitations
Describe how simulated outcomes are generated. If labels are assigned independently of input features, the model has no genuine predictive signal; document this and do not overstate performance. This synthetic model is not suitable for real insurance decisions.

## Final checklist
- [ ] 300–500 rows, all required columns, no unintended nulls.
- [ ] Approximate 70/20/10 class mix.
- [ ] Stratified train/test split.
- [ ] At least two engineered features.
- [ ] No test-label leakage.
- [ ] Saved artifact includes preprocessing and classifier.
- [ ] Actual per-class metrics and confusion matrix.
- [ ] Weakest class and improvement documented.
- [ ] API returns all three probabilities.
- [ ] Missing/invalid inputs return clear 4xx errors.
- [ ] Fresh-environment run verified before GitHub push.
