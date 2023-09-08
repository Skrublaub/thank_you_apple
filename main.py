import sqlite3
import argparse


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("-i", "--index", type=int)
    args = parser.parse_args()

    con: sqlite3.Connection = sqlite3.connect("vimusic_temp.db")
    curs: sqlite3.Cursor = con.cursor()

    song_info: list[tuple[str, str]] = curs.execute("select title, artistsText from Song s inner join SongPlaylistMap spm on songid=id;").fetchall()

    curs.close()
    
    # for title, artist in song_info:
    if args.index < len(song_info):
        print(f"{song_info[args.index][0]} {song_info[args.index][1]}")
    else:
        print("done")

    return


if __name__ == "__main__":
    main()