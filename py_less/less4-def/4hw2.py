def make_album(artist_name, album_name, number_tracks=None):
    if number_tracks:
        about_album = {'artist': artist_name, 'album': album_name, 'tracks': number_tracks}
    else:
        about_album = {'artist': artist_name, 'album': album_name}
    return about_album
ma = make_album('linkin park', 'in the end', 22)
print(ma)

ma = make_album('radius21', 'shekspir')
print(ma)

ma = make_album('bumbox', 'vahteram')
print(ma)

ma = make_album('shoxrux', 'ona', 15)
print(ma)

while True:
    print('\nВвод данных для альбома \nДля выхода введите \'q\'')
    artist = input('Введите имя исполнителя: ')
    if artist == 'q':
        break
    album = input('Название альбома: ')
    if artist == 'q':
        break
    ma = make_album(artist_name=artist, album_name=album)
    print(ma)




