# def mov_up():
#     global mov_coor
#     x = mov_coor[1]
#     y = mov_coor[0]
#     if y - 1 == -1:
#         make_maze()
#         print("It's the end of the Universe!")


#     else:
#         y -= 1
#         mov_coor = [y,x]
#         print("up")
#         return mov_coor

# # def move_UP():
# #     global mov_coor
# #     x = mov_coor[1]
# #     y = mov_coor[0]
# #     y -= 1
# #     mov_coor = [y,x]
# #     return mov_coor

# def mov_left():
#     global mov_coor
#     x = mov_coor[1]
#     y = mov_coor[0]
#     if x - 1 == 30:
#         make_maze()
#         print("It's the end of the Universe!")


#     else:
#         x -= 1
#         mov_coor = [y,x]
#         print("Left")
#         return mov_coor

# def mov_down():
#     global mov_coor
#     x = mov_coor[1]
#     y = mov_coor[0]
#     if y - 1 == 30:
#         make_maze()
#         print("It's the end of the Universe!")
#         print("Go Up, Left or Right")


#     else:
#         x += 1
#         mov_coor = [y,x]
#         print("down")
#         return mov_coor

# def mov_right():
#     global mov_coor
#     x = mov_coor[1]
#     y = mov_coor[0]
#     if x + 1 == 30:
#         make_maze()
#         print("It's the end of the Universe!")
#         print("Go Up, Left or Right")


#     else:
#         y += 1
#         mov_coor = [y,x]
#         mov_coor[1] += 1           # I think x+1 is ->
#         print("right")
#         return mov_coor

a = [1,2]
b = tuple(abc)

c = list(b)
