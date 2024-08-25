import pandas as pd
import matplotlib.pyplot as plt
 
# Load the dataset
df = pd.read_csv('data_wrangling_medical_2024_u7568823.csv')

# Extract relevant columns
bmi = df['bmi']
age = df['age_at_consultation']

# Create a hexbin plot
plt.figure(figsize=(10, 6))
plt.hexbin(age, bmi, gridsize=30, cmap='Blues', mincnt=1)
plt.colorbar(label='Count in bin')
plt.title('Hexbin Plot of BMI vs Age at Consultation')
plt.xlabel('Age at Consultation')
plt.ylabel('BMI')
plt.grid(True)

# Show the plot
plt.show()
