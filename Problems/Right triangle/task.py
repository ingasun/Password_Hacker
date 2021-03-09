class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = (leg_1 * leg_2) / 2
        # calculate the area here


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
rechteck = RightTriangle(input_c, input_a, input_b)
if(input_a ** 2 + input_b ** 2 == input_c ** 2):
    print(rechteck.area)
else:
    print('Not right')


#     def __init__(self, hyp, leg_1, leg_2):
#         self.c = hyp
#         self.a = leg_1
#         self.b = leg_2
#         self.area = (leg_1 * leg_2) / 2
#
# input_c, input_a, input_b = [int(x) for x in
#                              input().split()]  # Here the IDE shows me an error, I can put only one number
#
# triangle = RightTriangle(input_c, input_a, input_b)
#
# if input_c ** 2 == input_a ** 2 + input_b ** 2:
#     print(triangle.area)
# else:
#     print("Not right")