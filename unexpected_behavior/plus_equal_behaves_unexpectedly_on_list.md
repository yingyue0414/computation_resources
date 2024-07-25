The general answer is that += tries to call the __iadd__ special method, and if that isn't available it tries to use __add__ instead. So the issue is with the difference between these special methods.

The __iadd__ special method is for an in-place addition, that is it mutates the object that it acts on. The __add__ special method returns a new object and is also used for the standard + operator.

So when the += operator is used on an object which has an __iadd__ defined the object is modified in place. Otherwise it will instead try to use the plain __add__ and return a new object.

That is why for mutable types like lists += changes the object's value, whereas for immutable types like tuples, strings and integers a new object is returned instead (a += b becomes equivalent to a = a + b).

For types that support both __iadd__ and __add__ you therefore have to be careful which one you use. a += b will call __iadd__ and mutate a, whereas a = a + b will create a new object and assign it to a. They are not the same operation!

Source: https://stackoverflow.com/questions/2347265/why-does-behave-unexpectedly-on-lists
