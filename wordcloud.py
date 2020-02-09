# -*- coding: utf-8 -*-
from wordcloud import WordCloud
from konlpy.tag import Okt
import matplotlib.pyplot as plt
import operator

okt = Okt()


# 문장 분석 (명사만 가져오기)
def analyze():
    text = '애국가의 자취는 개화기(조선말) 갑오개혁 직후까지 올라간다. ' \
           '1896년 당시 독립문 정초식에서 배재학당 학생들에 의해 그 유명한 스코틀랜드 민요 올드 랭 사인의 멜로디로 불린 작사 미상인 애국가가 최초의 애국가로 여겨진다.' \
           ' 여기서 후렴 "무궁화 삼천리 화려강산 죠션 사람 죠션으로 길이 보죤하세" 라는 가사가 지금의 애국가 가사에서도 맥을 이어 변형(조선→대한)되어 쓰이고 있는 데서 확인할 수 있다.' \
           ' 이 때는 한 해에 수십개의 애국가가 쏟아져나왔다.' \
           '대한제국의 애국가는 1898년 가사가 기초되어 이때는 God Save the King에 맞춰 불렀다.' \
           ' 이후 1902년 완성한 에케르트 작곡의 "대한제국 애국가"가 공식적으로 대한제국의 애국가가 되었다. ' \
           '이후 공식적으로는 1907년 순종 황제 즉위식에서 마지막으로 연주되었고, 1909년에 이르러서는 일제의 애국 창가(唱歌)에 대한 단속으로 인해 7년만에 금지곡이 된 비운의 국가이다.'

    li = okt.nouns(text)
    dic = {}

    # 명사 빈도수 세기
    for word in li:
        if (word in dic) is True:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1

    # 빈도수가 많은 것으로 정렬
    sort_dict = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)

    return_li = []
    count = 0

    # 상위 20개 단어만 반환
    for item in sort_dict:
        for i in range(item[1]):
            return_li.append(item[0])
        count += 1
        if count == 20:
            break

    return return_li


# word cloud 그리기
def draw():
    data = analyze()
    text = ''

    for item in data:
        text += item + ' '

    print(text)

    wc = WordCloud(background_color='white',
                   width=800,
                   height=600,
                   max_words=20,  # 표현 단어 수
                   font_path='/Library/Fonts/AppleGothic.ttf',  # 폰트 경로 지정 -> macOS인 경우
                   )

    cloud = wc.generate_from_text(text)
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    draw()