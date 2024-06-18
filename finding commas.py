def count_commas(N):
    total_commas=0
    if N>=1000:
        total_commas +=min(N,999999)-999
    if N>=1000000:
        total_commas +=(min(N,999999999)-999999)*2
    if N>=1000000000:
        total_commas +=(min(N,999999999999)-999999999)*3
    return total_commas
print(count_commas(5000))