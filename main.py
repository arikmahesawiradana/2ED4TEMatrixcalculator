try:
    import kelompok3_2ED4TE as arik
except:
    print("you have to download library first")

#definisikan soal disini
nomor1 = [[1,2,3], [4,50,6], [7,8,9]]
nomor2 = [[1,2,3], [4,50,6], [7,8,9]]
nomor3 = [[1,2,3], [4,50,6], [7,8,9]]
nomor4 = [[1,2,3], [4,50,6], [7,8,9]]
nomor5 = [[1,2,3], [4,50,6], [7,8,9]]
#rubah kedalam matrix
matrix1 = arik.numpyMatrix(nomor1)
matrix2 = arik.numpyMatrix(nomor2)
matrix3 = arik.numpyMatrix(nomor3)
matrix4 = arik.numpyMatrix(nomor4)
matrix5 = arik.numpyMatrix(nomor5)
#definisikan soal
def soal (matrix):
    det = matrix
    #callback program determine
    hasildet = det.determine()
    #callback program joint
    hasiladj = det.adjoint()
    print("determinan:")
    print(hasildet)
    print("adjoint:")
    print(hasiladj)
    print("")

#program main
if __name__ == '__main__':
    soal(matrix1)
    soal(matrix2)
    soal(matrix3)
    soal(matrix4)
    soal(matrix5)