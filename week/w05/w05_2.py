#파일 불러오기?
#.strtp()은 줄바꿈을 없에준다 보이지는 않지만 html마냥 출력될 때는 보이지 않는 기호가 있는듯
def readfile():
    with open("파일경로이름") as f:
        data = []
        for line in f:
            text = line.strip()
            print(f"!{filename}!")
        return data