import graphlab


sales = graphlab.SFrame('D:\Tasks\projects\python\casestudy\course1\home_data.gl/')
train_data, test_data = sales.random_split(.8, seed=0)
sqft_model = graphlab.linear_regression.create(train_data)
print(train_data.head(5))
