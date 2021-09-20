name = "Bernard Bruna"
print(name)

cube_user = int(input("Input your measurements for cube here: "))
tetra_user = int(input("Input your measurements for tetrahedron here: "))

def v_cube(cube):
    volume = cube_user ** 3
    return volume
answer_cube = v_cube(cube_user)
print(answer_cube)

def v_tetra(tetra):
    vol_t = tetra_user ** 3 / 6 + 2 ** 0.5
    return vol_t
answer_tetra = v_tetra(tetra_user)
print(answer_tetra)














