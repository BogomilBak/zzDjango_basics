def check_if_triplet_exists_in_matrix(triplet_sorted, matrix):
    if triplet_sorted in matrix:
        return True

    return False


def check_if_requirements_are_met(i, j, k):
    if (i + j + k == 0) and \
            i != j and \
            i != k and \
            j != k:

        return True


def threeSum(nums):
    matrix = []
    for index1 in range(len(nums)):

        for index2 in range(len(nums)):
            if index1 == index2:
                continue

            for index3 in range(len(nums)):
                if index1 == index3 or index2 == index3:
                    continue

                i = nums[index1]
                j = nums[index2]
                k = nums[index3]

                validation = check_if_requirements_are_met(i, j, k)

                if validation:

                    triplet = [i, j, k]
                    triplet_sorted = sorted(triplet)
                    if not matrix:
                        matrix.append(triplet_sorted)
                        continue

                    validation = check_if_triplet_exists_in_matrix(triplet_sorted, matrix)

                    if not validation:
                        matrix.append(triplet_sorted)

    return matrix


print(threeSum([-1, 0, 1, 2, -1, -4]))
