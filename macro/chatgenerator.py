first = ['디스코드','다들','채팅','레벨업','챗굴','쳇굴','화리','로드맵','프로젝트','화력','사람들','선점']
last = ['뭐야','무야','모야','엄청나네','대박이네','대박','쩔어','무야무야','뭐야뭐야']

middle = ''

stringlist = []

for i in first:
	for j in last:
		stringlist.append(i +  middle + j)

for _ in stringlist:
	print(_)