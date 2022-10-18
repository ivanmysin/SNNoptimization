import tensorflow as tf

class MyTest(tf.keras.Model):
    def __init__(self):
        super(MyTest, self).__init__()

        self.x = tf.Variable(3.0, dtype=tf.float64)
        self.y = tf.Variable(1.0, dtype=tf.float64)

        self.lamda_x = tf.Variable(10**6, dtype=tf.float64, trainable=False)
        #self.lamda_y = tf.Variable(1.0, dtype=tf.float64)

def Loss(x, y, lamda_x):
    l = x**2 + 4*y**2 + lamda_x * tf.nn.relu( (x - 0.5) )

    return l


model = MyTest()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)



for i in range(5000):
    with tf.GradientTape() as tape:
        loss = Loss(model.x, model.y, model.lamda_x) #, model.lamda_y,
        grad = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(grad, model.trainable_variables))

print(model.x.numpy())
print(model.y.numpy())
print(model.lamda_x.numpy())
#print(model.lamda_y.numpy())