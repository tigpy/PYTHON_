class ExampleClass:
       def function1(parameters):
          print("function1() executing...")
          def function2(parameters):
             print("function2() executing...")
             ob1 = ExampleClass()
             ob1.function1()
             ob1.function2()