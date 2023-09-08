import sqlite3

con: sqlite3.Connection = sqlite3.connect("vimusic_temp.db")
curs: sqlite3.Cursor = con.cursor()

song_info: list[tuple[str, str]] = curs.execute("select title, artistsText from Song s inner join SongPlaylistMap spm on songid=id;").fetchall()

curs.close()

song_titles = song_info