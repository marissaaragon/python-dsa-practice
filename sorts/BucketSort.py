# Bucket Sort

def bucked_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    num_buckets = len(arr)

    if max_val == min_val:
        return arr

    bucket_range = (max_val - min_val) / num_buckets
    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        if num == max_val:
            bucket_index = num_buckets - 1
        else:
            bucket_index = int((num - min_val) / bucket_range)
        buckets[bucket_index].append(num)

    sorted_arr = []
    for bucket in buckets:
        bucket.sort()
        sorted_arr.extend(bucket)

    return sorted_arr