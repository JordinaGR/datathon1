import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/home/jordina/Desktop/datathon/out.csv')

df['MitjaPersones'].index = [i/2 for i in range(len(df))]

plt.scatter(df.index, df['MitjaPersones'], s=10, alpha=0.8, edgecolors='w')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of DataFrame')

# Show the plot
plt.show()