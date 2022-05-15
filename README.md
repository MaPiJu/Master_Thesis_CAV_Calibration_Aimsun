# Master_Thesis_CAV_Calibration_Aimsun

This repositery contains the files needed to reproduce the secenario 2 of the Master Thesis "Methodology Development for the Calibration of Microscopic Traffic Simulations Focusing on Connected Automated Driving".

The Microscopic Traffic Simulation is made with AIMSUN.

To reproduce the experiment, open the Aimsun file "Master's Thesis Network".

**1st Synthetic Calibration Data Production:**

Select the API files "WU Read_Aggregated_Detectors.py" in the Dynamic Scenario 37524.
\nIn the GUI run the Python script: "WU No Distinct Synth Data Production"


**2nd Synthetic Validation Data Production:**

Select the API files "WU Validation Syn prod data Read_Aggregated_Detectors.py" in the Dynamic Scenario 37524.
In the GUI run the Python script: "WU Vali No Distinct Synth Data Production"


**3rd Sequential Calibration of CAV and HDV:**

Select the API files "WU Read_Aggregated_Detectors - Calibration.py" in the Dynamic Scenario 37524.
In the GUI run the Python script: "WU CAV & HDV cali"

**4th Validation:**

Select the API files "WU Read_Aggregated_Detectors - Validation.py" in the Dynamic Scenario 37524.
In the GUI run the Python script: "WU validation no difference"
