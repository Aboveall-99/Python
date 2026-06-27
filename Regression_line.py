import pandas as pd
from sklearn.linear_model import LinearRegression


advert_data = {
    "tv": [23000, 44000, 17000, 15000, 18000, 87000, 57000],
    "radio": [37000, 39000, 45000, 41000, 36000, 28000, 42000],
    "sales": [221000, 304000, 197000, 188000, 215000, 450000, 365000]
}
df = pd.DataFrame(advert_data)


X = df[['tv', 'radio']]
y = df['sales']


model = LinearRegression()
model.fit(X, y)

print(f"Baseline Sales (Intercept): ${model.intercept_:.2f}")
print(f"TV Coefficient: {model.coef_[0]:.4f}")
print(f"Radio Coefficient: {model.coef_[1]:.4f}")
print(f"Model Accuracy (R-squared): {model.score(X, y):.4f}\n")


new_budget = pd.DataFrame({'tv': [50000], 'radio': [30000]})
predicted_sales = model.predict(new_budget)

print(f"Predicted Sales for $50k TV / $30k Radio: ${predicted_sales[0]:.2f}")
