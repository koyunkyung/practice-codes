def solution(genres, plays):
    answer = []
    total = {}  # {장르: 총 재생 횟수}
    genre = {}  # {장르: [(플레이 횟수, 고유번호)]}
    
    for i in range(len(genres)):
        total[genres[i]] = total.get(genres[i], 0) + plays[i]
        genre[genres[i]] = genre.get(genres[i], []) + [(plays[i], i)]
    
    genSort = sorted(total.items(), key=lambda x: x[1], reverse=True)
    
    for (gen, totalPlay) in genSort:
        genre[gen] = sorted(genre[gen], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in genre[gen][:2]]
    
    return answer