
import pandas as pd

# Load the Excel file
file_path = "attendance.xlsx"
df = pd.read_excel(file_path)

# Identify employees with attendance < 80%
low_attendance = df[df['Attendance (%)'] < 80]

# Calculate average attendance
average_attendance = df['Attendance (%)'].mean()

# Add insights to the Excel
df.loc['Average'] = ["Average", average_attendance]

# Save the results
low_attendance.to_excel("low_attendance.xlsx", index=False)
df.to_excel("attendance_summary.xlsx", index=False)

print("Attendance analysis saved!")
