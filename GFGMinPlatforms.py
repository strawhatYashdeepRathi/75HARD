

def countPlatforms(arr, dep):
    arr.sort()
    dep.sort()
    res = 1
    plt = 1
    i, j = 1, 0
    while i < len(arr) and j < len(dep):
        if arr[i] > dep[j]:
            j+=1
            plt-=1
        else:
            plt+=1
            i+=1
        res = max(res, plt)
    return res
        


if __name__ == "__main__":
    arr = [900, 945, 955, 1100, 1500, 1800]
    dep = [920, 1200, 1130, 1150, 1900, 2000]
    print("Minimum number of Platforms required ", countPlatforms(arr, dep))