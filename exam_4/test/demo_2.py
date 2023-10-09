def check_if_valid(i, j, k):
    if i + j + k == 0:
        return True


def check_if_exists(triplet, matrix):
    if triplet not in matrix:
        return True


def threeSum(nums):
    matrix = []
    sorted_nums = sorted(nums)
    for index in range(len(sorted_nums) - 1):
        i = index
        j = index + 1
        k = len(sorted_nums) - 1

        i_number = sorted_nums[i]
        j_number = sorted_nums[j]
        k_number = sorted_nums[k]

        while j_number < k_number:

            j_number = sorted_nums[j]
            k_number = sorted_nums[k]

            if check_if_valid(i_number, j_number, k_number):

                triplet = sorted([i_number, j_number, k_number])

                if not matrix:
                    matrix.append(triplet)
                else:
                    if check_if_exists(triplet, matrix):
                        matrix.append(triplet)

                break

            j += 1
            k -= 1



    print(matrix)





print(threeSum([-1, 0, 1, 2, -1, -4]))
