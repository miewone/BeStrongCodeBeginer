def solution(s):
    zero_cnt = 0
    bin_cnt = 0
    while s != '1':
        if '0' in s:
            zero_cnt += s.count('0')
            s = s.replace('0','')
        s = str(format(len(s),'b'))
        bin_cnt += 1
    answer = [bin_cnt, zero_cnt]
    return answer
