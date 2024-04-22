import tkinter as tk
import random
import snakeAndLadderBase64OfPics
from threading import *
from tkinter import messagebox
from pygame import mixer

class SnakesAndLadder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x700")
        self.root.resizable(0,0)
        self.root.config(bg="#e5cbc2")
        self.root.title("Snake & Ladder")
        self.mainFrame = tk.Frame(self.root,bg="#e5cbc2")
        self.mainFrame.pack(pady=20)
        # Initializing variables to start new game
        self.player1Turn = True
        self.player2Turn = False
        self.player1Position = self.player2Position = 0
        self.prevPlayer1Position = self.prevPlayer2Position = 0
        self.gameOver = False
        # ladder tiles map
        self.ladderMap = {2:23,7:29,22:41,28:77,30:32,44:58,54:69,70:90,74:92,80:83}
        # snake tiles map
        self.snakesMap = {27:7,35:5,39:3,50:34,59:46,66:24,73:12,76:63,89:67,97:86,99:25}
        # Initially when the game loads the sound is ON
        self.allSoundActive = True

        self.frameLeft = tk.Frame(self.mainFrame,bg="#e5cbc2")
        self.frameLeft.grid(row=0,column=0)
        self.window = tk.Frame(self.mainFrame)
        self.window.grid(row=0,column=1)
        self.frameRight = tk.Frame(self.mainFrame,bg="#e5cbc2")
        self.frameRight.grid(row=0,column=2)

        #pictures converted to PhotoImage
        self.snakesAndLaddersIcon = tk.PhotoImage(data=snakeAndLadderBase64OfPics.snakesAndLadderAppIcon)
        self.playAgainButtonImage = tk.PhotoImage(data=snakeAndLadderBase64OfPics.playAgainButton).subsample(2,2)
        self.exitGameButtonImage = tk.PhotoImage(data=snakeAndLadderBase64OfPics.exitWoodenImage).subsample(2,2)
        self.diceButtonIcon = tk.PhotoImage(data=snakeAndLadderBase64OfPics.diceRedIcon)
        self.winnerBoardPicture = tk.PhotoImage(data=snakeAndLadderBase64OfPics.winnerBoard).subsample(2,2)
        self.winnerBoardRedPicture = tk.PhotoImage(data=snakeAndLadderBase64OfPics.winnerRedBoard).subsample(2,2)
        self.winnerBoardBluePicture = tk.PhotoImage(data=snakeAndLadderBase64OfPics.winnerBlueBoard).subsample(2,2)
        self.soundOnPicture = tk.PhotoImage(data=snakeAndLadderBase64OfPics.sound_On_Button).subsample(2,2)
        self.soundOffPicture = tk.PhotoImage(data=snakeAndLadderBase64OfPics.sound_Off_Button).subsample(2,2)
        self.player1Piece = tk.PhotoImage(file="player1_red_piece.png")
        self.player2Piece = tk.PhotoImage(file="player2_blue_piece.png")
        self.player1PieceSmall = tk.PhotoImage(file="player1_red_piece.png").subsample(2,2)
        self.player2PieceSmall = tk.PhotoImage(file="player2_blue_piece.png").subsample(2,2)
        self.diceFace1 = tk.PhotoImage(file="faces-one.png")
        self.diceFace2 = tk.PhotoImage(file="faces-two.png")
        self.diceFace3 = tk.PhotoImage(file="faces-three.png")
        self.diceFace4 = tk.PhotoImage(file="faces-four.png")
        self.diceFace5 = tk.PhotoImage(file="faces-five.png")
        self.diceFace6 = tk.PhotoImage(file="faces-six.png")
        # Picture of empty tiles converted to PhotoImage
        self.tile1 = tk.PhotoImage(file="./noPiecesOnTile/tile1.png").subsample(2,2)
        self.tile2 = tk.PhotoImage(file="./noPiecesOnTile/tile2.png").subsample(2,2)
        self.tile3 = tk.PhotoImage(file="./noPiecesOnTile/tile3.png").subsample(2,2)
        self.tile4 = tk.PhotoImage(file="./noPiecesOnTile/tile4.png").subsample(2,2)
        self.tile5 = tk.PhotoImage(file="./noPiecesOnTile/tile5.png").subsample(2,2)
        self.tile6 = tk.PhotoImage(file="./noPiecesOnTile/tile6.png").subsample(2,2)
        self.tile7 = tk.PhotoImage(file="./noPiecesOnTile/tile7.png").subsample(2,2)
        self.tile8 = tk.PhotoImage(file="./noPiecesOnTile/tile8.png").subsample(2,2)
        self.tile9 = tk.PhotoImage(file="./noPiecesOnTile/tile9.png").subsample(2,2)
        self.tile10 = tk.PhotoImage(file="./noPiecesOnTile/tile10.png").subsample(2,2)
        self.tile11 = tk.PhotoImage(file="./noPiecesOnTile/tile11.png").subsample(2,2)
        self.tile12 = tk.PhotoImage(file="./noPiecesOnTile/tile12.png").subsample(2,2)
        self.tile13 = tk.PhotoImage(file="./noPiecesOnTile/tile13.png").subsample(2,2)
        self.tile14 = tk.PhotoImage(file="./noPiecesOnTile/tile14.png").subsample(2,2)
        self.tile15 = tk.PhotoImage(file="./noPiecesOnTile/tile15.png").subsample(2,2)
        self.tile16 = tk.PhotoImage(file="./noPiecesOnTile/tile16.png").subsample(2,2)
        self.tile17 = tk.PhotoImage(file="./noPiecesOnTile/tile17.png").subsample(2,2)
        self.tile18 = tk.PhotoImage(file="./noPiecesOnTile/tile18.png").subsample(2,2)
        self.tile19 = tk.PhotoImage(file="./noPiecesOnTile/tile19.png").subsample(2,2)
        self.tile20 = tk.PhotoImage(file="./noPiecesOnTile/tile20.png").subsample(2,2)
        self.tile21 = tk.PhotoImage(file="./noPiecesOnTile/tile21.png").subsample(2,2)
        self.tile22 = tk.PhotoImage(file="./noPiecesOnTile/tile22.png").subsample(2,2)
        self.tile23 = tk.PhotoImage(file="./noPiecesOnTile/tile23.png").subsample(2,2)
        self.tile24 = tk.PhotoImage(file="./noPiecesOnTile/tile24.png").subsample(2,2)
        self.tile25 = tk.PhotoImage(file="./noPiecesOnTile/tile25.png").subsample(2,2)
        self.tile26 = tk.PhotoImage(file="./noPiecesOnTile/tile26.png").subsample(2,2)
        self.tile27 = tk.PhotoImage(file="./noPiecesOnTile/tile27.png").subsample(2,2)
        self.tile28 = tk.PhotoImage(file="./noPiecesOnTile/tile28.png").subsample(2,2)
        self.tile29 = tk.PhotoImage(file="./noPiecesOnTile/tile29.png").subsample(2,2)
        self.tile30 = tk.PhotoImage(file="./noPiecesOnTile/tile30.png").subsample(2,2)
        self.tile31 = tk.PhotoImage(file="./noPiecesOnTile/tile31.png").subsample(2,2)
        self.tile32 = tk.PhotoImage(file="./noPiecesOnTile/tile32.png").subsample(2,2)
        self.tile33 = tk.PhotoImage(file="./noPiecesOnTile/tile33.png").subsample(2,2)
        self.tile34 = tk.PhotoImage(file="./noPiecesOnTile/tile34.png").subsample(2,2)
        self.tile35 = tk.PhotoImage(file="./noPiecesOnTile/tile35.png").subsample(2,2)
        self.tile36 = tk.PhotoImage(file="./noPiecesOnTile/tile36.png").subsample(2,2)
        self.tile37 = tk.PhotoImage(file="./noPiecesOnTile/tile37.png").subsample(2,2)
        self.tile38 = tk.PhotoImage(file="./noPiecesOnTile/tile38.png").subsample(2,2)
        self.tile39 = tk.PhotoImage(file="./noPiecesOnTile/tile39.png").subsample(2,2)
        self.tile40 = tk.PhotoImage(file="./noPiecesOnTile/tile40.png").subsample(2,2)
        self.tile41 = tk.PhotoImage(file="./noPiecesOnTile/tile41.png").subsample(2,2)
        self.tile42 = tk.PhotoImage(file="./noPiecesOnTile/tile42.png").subsample(2,2)
        self.tile43 = tk.PhotoImage(file="./noPiecesOnTile/tile43.png").subsample(2,2)
        self.tile44 = tk.PhotoImage(file="./noPiecesOnTile/tile44.png").subsample(2,2)
        self.tile45 = tk.PhotoImage(file="./noPiecesOnTile/tile45.png").subsample(2,2)
        self.tile46 = tk.PhotoImage(file="./noPiecesOnTile/tile46.png").subsample(2,2)
        self.tile47 = tk.PhotoImage(file="./noPiecesOnTile/tile47.png").subsample(2,2)
        self.tile48 = tk.PhotoImage(file="./noPiecesOnTile/tile48.png").subsample(2,2)
        self.tile49 = tk.PhotoImage(file="./noPiecesOnTile/tile49.png").subsample(2,2)
        self.tile50 = tk.PhotoImage(file="./noPiecesOnTile/tile50.png").subsample(2,2)
        self.tile51 = tk.PhotoImage(file="./noPiecesOnTile/tile51.png").subsample(2,2)
        self.tile52 = tk.PhotoImage(file="./noPiecesOnTile/tile52.png").subsample(2,2)
        self.tile53 = tk.PhotoImage(file="./noPiecesOnTile/tile53.png").subsample(2,2)
        self.tile54 = tk.PhotoImage(file="./noPiecesOnTile/tile54.png").subsample(2,2)
        self.tile55 = tk.PhotoImage(file="./noPiecesOnTile/tile55.png").subsample(2,2)
        self.tile56 = tk.PhotoImage(file="./noPiecesOnTile/tile56.png").subsample(2,2)
        self.tile57 = tk.PhotoImage(file="./noPiecesOnTile/tile57.png").subsample(2,2)
        self.tile58 = tk.PhotoImage(file="./noPiecesOnTile/tile58.png").subsample(2,2)
        self.tile59 = tk.PhotoImage(file="./noPiecesOnTile/tile59.png").subsample(2,2)
        self.tile60 = tk.PhotoImage(file="./noPiecesOnTile/tile60.png").subsample(2,2)
        self.tile61 = tk.PhotoImage(file="./noPiecesOnTile/tile61.png").subsample(2,2)
        self.tile62 = tk.PhotoImage(file="./noPiecesOnTile/tile62.png").subsample(2,2)
        self.tile63 = tk.PhotoImage(file="./noPiecesOnTile/tile63.png").subsample(2,2)
        self.tile64 = tk.PhotoImage(file="./noPiecesOnTile/tile64.png").subsample(2,2)
        self.tile65 = tk.PhotoImage(file="./noPiecesOnTile/tile65.png").subsample(2,2)
        self.tile66 = tk.PhotoImage(file="./noPiecesOnTile/tile66.png").subsample(2,2)
        self.tile67 = tk.PhotoImage(file="./noPiecesOnTile/tile67.png").subsample(2,2)
        self.tile68 = tk.PhotoImage(file="./noPiecesOnTile/tile68.png").subsample(2,2)
        self.tile69 = tk.PhotoImage(file="./noPiecesOnTile/tile69.png").subsample(2,2)
        self.tile70 = tk.PhotoImage(file="./noPiecesOnTile/tile70.png").subsample(2,2)
        self.tile71 = tk.PhotoImage(file="./noPiecesOnTile/tile71.png").subsample(2,2)
        self.tile72 = tk.PhotoImage(file="./noPiecesOnTile/tile72.png").subsample(2,2)
        self.tile73 = tk.PhotoImage(file="./noPiecesOnTile/tile73.png").subsample(2,2)
        self.tile74 = tk.PhotoImage(file="./noPiecesOnTile/tile74.png").subsample(2,2)
        self.tile75 = tk.PhotoImage(file="./noPiecesOnTile/tile75.png").subsample(2,2)
        self.tile76 = tk.PhotoImage(file="./noPiecesOnTile/tile76.png").subsample(2,2)
        self.tile77 = tk.PhotoImage(file="./noPiecesOnTile/tile77.png").subsample(2,2)
        self.tile78 = tk.PhotoImage(file="./noPiecesOnTile/tile78.png").subsample(2,2)
        self.tile79 = tk.PhotoImage(file="./noPiecesOnTile/tile79.png").subsample(2,2)
        self.tile80 = tk.PhotoImage(file="./noPiecesOnTile/tile80.png").subsample(2,2)
        self.tile81 = tk.PhotoImage(file="./noPiecesOnTile/tile81.png").subsample(2,2)
        self.tile82 = tk.PhotoImage(file="./noPiecesOnTile/tile82.png").subsample(2,2)
        self.tile83 = tk.PhotoImage(file="./noPiecesOnTile/tile83.png").subsample(2,2)
        self.tile84 = tk.PhotoImage(file="./noPiecesOnTile/tile84.png").subsample(2,2)
        self.tile85 = tk.PhotoImage(file="./noPiecesOnTile/tile85.png").subsample(2,2)
        self.tile86 = tk.PhotoImage(file="./noPiecesOnTile/tile86.png").subsample(2,2)
        self.tile87 = tk.PhotoImage(file="./noPiecesOnTile/tile87.png").subsample(2,2)
        self.tile88 = tk.PhotoImage(file="./noPiecesOnTile/tile88.png").subsample(2,2)
        self.tile89 = tk.PhotoImage(file="./noPiecesOnTile/tile89.png").subsample(2,2)
        self.tile90 = tk.PhotoImage(file="./noPiecesOnTile/tile90.png").subsample(2,2)
        self.tile91 = tk.PhotoImage(file="./noPiecesOnTile/tile91.png").subsample(2,2)
        self.tile92 = tk.PhotoImage(file="./noPiecesOnTile/tile92.png").subsample(2,2)
        self.tile93 = tk.PhotoImage(file="./noPiecesOnTile/tile93.png").subsample(2,2)
        self.tile94 = tk.PhotoImage(file="./noPiecesOnTile/tile94.png").subsample(2,2)
        self.tile95 = tk.PhotoImage(file="./noPiecesOnTile/tile95.png").subsample(2,2)
        self.tile96 = tk.PhotoImage(file="./noPiecesOnTile/tile96.png").subsample(2,2)
        self.tile97 = tk.PhotoImage(file="./noPiecesOnTile/tile97.png").subsample(2,2)
        self.tile98 = tk.PhotoImage(file="./noPiecesOnTile/tile98.png").subsample(2,2)
        self.tile99 = tk.PhotoImage(file="./noPiecesOnTile/tile99.png").subsample(2,2)
        self.tile100 = tk.PhotoImage(file="./noPiecesOnTile/tile100.png").subsample(2,2)

        # Player 1 (Red)
        self.tileRed1 = tk.PhotoImage(file="./redpiecesontile/1.png").subsample(2,2)
        self.tileRed2 = tk.PhotoImage(file="./redpiecesontile/2.png").subsample(2,2)
        self.tileRed3 = tk.PhotoImage(file="./redpiecesontile/3.png").subsample(2,2)
        self.tileRed4 = tk.PhotoImage(file="./redpiecesontile/4.png").subsample(2,2)
        self.tileRed5 = tk.PhotoImage(file="./redpiecesontile/5.png").subsample(2,2)
        self.tileRed6 = tk.PhotoImage(file="./redpiecesontile/6.png").subsample(2,2)
        self.tileRed7 = tk.PhotoImage(file="./redpiecesontile/7.png").subsample(2,2)
        self.tileRed8 = tk.PhotoImage(file="./redpiecesontile/8.png").subsample(2,2)
        self.tileRed9 = tk.PhotoImage(file="./redpiecesontile/9.png").subsample(2,2)
        self.tileRed10 = tk.PhotoImage(file="./redpiecesontile/10.png").subsample(2,2)
        self.tileRed11 = tk.PhotoImage(file="./redpiecesontile/11.png").subsample(2,2)
        self.tileRed12 = tk.PhotoImage(file="./redpiecesontile/12.png").subsample(2,2)
        self.tileRed13 = tk.PhotoImage(file="./redpiecesontile/13.png").subsample(2,2)
        self.tileRed14 = tk.PhotoImage(file="./redpiecesontile/14.png").subsample(2,2)
        self.tileRed15 = tk.PhotoImage(file="./redpiecesontile/15.png").subsample(2,2)
        self.tileRed16 = tk.PhotoImage(file="./redpiecesontile/16.png").subsample(2,2)
        self.tileRed17 = tk.PhotoImage(file="./redpiecesontile/17.png").subsample(2,2)
        self.tileRed18 = tk.PhotoImage(file="./redpiecesontile/18.png").subsample(2,2)
        self.tileRed19 = tk.PhotoImage(file="./redpiecesontile/19.png").subsample(2,2)
        self.tileRed20 = tk.PhotoImage(file="./redpiecesontile/20.png").subsample(2,2)
        self.tileRed21 = tk.PhotoImage(file="./redpiecesontile/21.png").subsample(2,2)
        self.tileRed22 = tk.PhotoImage(file="./redpiecesontile/22.png").subsample(2,2)
        self.tileRed23 = tk.PhotoImage(file="./redpiecesontile/23.png").subsample(2,2)
        self.tileRed24 = tk.PhotoImage(file="./redpiecesontile/24.png").subsample(2,2)
        self.tileRed25 = tk.PhotoImage(file="./redpiecesontile/25.png").subsample(2,2)
        self.tileRed26 = tk.PhotoImage(file="./redpiecesontile/26.png").subsample(2,2)
        self.tileRed27 = tk.PhotoImage(file="./redpiecesontile/27.png").subsample(2,2)
        self.tileRed28 = tk.PhotoImage(file="./redpiecesontile/28.png").subsample(2,2)
        self.tileRed29 = tk.PhotoImage(file="./redpiecesontile/29.png").subsample(2,2)
        self.tileRed30 = tk.PhotoImage(file="./redpiecesontile/30.png").subsample(2,2)
        self.tileRed31 = tk.PhotoImage(file="./redpiecesontile/31.png").subsample(2,2)
        self.tileRed32 = tk.PhotoImage(file="./redpiecesontile/32.png").subsample(2,2)
        self.tileRed33 = tk.PhotoImage(file="./redpiecesontile/33.png").subsample(2,2)
        self.tileRed34 = tk.PhotoImage(file="./redpiecesontile/34.png").subsample(2,2)
        self.tileRed35 = tk.PhotoImage(file="./redpiecesontile/35.png").subsample(2,2)
        self.tileRed36 = tk.PhotoImage(file="./redpiecesontile/36.png").subsample(2,2)
        self.tileRed37 = tk.PhotoImage(file="./redpiecesontile/37.png").subsample(2,2)
        self.tileRed38 = tk.PhotoImage(file="./redpiecesontile/38.png").subsample(2,2)
        self.tileRed39 = tk.PhotoImage(file="./redpiecesontile/39.png").subsample(2,2)
        self.tileRed40 = tk.PhotoImage(file="./redpiecesontile/40.png").subsample(2,2)
        self.tileRed41 = tk.PhotoImage(file="./redpiecesontile/41.png").subsample(2,2)
        self.tileRed42 = tk.PhotoImage(file="./redpiecesontile/42.png").subsample(2,2)
        self.tileRed43 = tk.PhotoImage(file="./redpiecesontile/43.png").subsample(2,2)
        self.tileRed44 = tk.PhotoImage(file="./redpiecesontile/44.png").subsample(2,2)
        self.tileRed45 = tk.PhotoImage(file="./redpiecesontile/45.png").subsample(2,2)
        self.tileRed46 = tk.PhotoImage(file="./redpiecesontile/46.png").subsample(2,2)
        self.tileRed47 = tk.PhotoImage(file="./redpiecesontile/47.png").subsample(2,2)
        self.tileRed48 = tk.PhotoImage(file="./redpiecesontile/48.png").subsample(2,2)
        self.tileRed49 = tk.PhotoImage(file="./redpiecesontile/49.png").subsample(2,2)
        self.tileRed50 = tk.PhotoImage(file="./redpiecesontile/50.png").subsample(2,2)
        self.tileRed51 = tk.PhotoImage(file="./redpiecesontile/51.png").subsample(2,2)
        self.tileRed52 = tk.PhotoImage(file="./redpiecesontile/52.png").subsample(2,2)
        self.tileRed53 = tk.PhotoImage(file="./redpiecesontile/53.png").subsample(2,2)
        self.tileRed54 = tk.PhotoImage(file="./redpiecesontile/54.png").subsample(2,2)
        self.tileRed55 = tk.PhotoImage(file="./redpiecesontile/55.png").subsample(2,2)
        self.tileRed56 = tk.PhotoImage(file="./redpiecesontile/56.png").subsample(2,2)
        self.tileRed57 = tk.PhotoImage(file="./redpiecesontile/57.png").subsample(2,2)
        self.tileRed58 = tk.PhotoImage(file="./redpiecesontile/58.png").subsample(2,2)
        self.tileRed59 = tk.PhotoImage(file="./redpiecesontile/59.png").subsample(2,2)
        self.tileRed60 = tk.PhotoImage(file="./redpiecesontile/60.png").subsample(2,2)
        self.tileRed61 = tk.PhotoImage(file="./redpiecesontile/61.png").subsample(2,2)
        self.tileRed62 = tk.PhotoImage(file="./redpiecesontile/62.png").subsample(2,2)
        self.tileRed63 = tk.PhotoImage(file="./redpiecesontile/63.png").subsample(2,2)
        self.tileRed64 = tk.PhotoImage(file="./redpiecesontile/64.png").subsample(2,2)
        self.tileRed65 = tk.PhotoImage(file="./redpiecesontile/65.png").subsample(2,2)
        self.tileRed66 = tk.PhotoImage(file="./redpiecesontile/66.png").subsample(2,2)
        self.tileRed67 = tk.PhotoImage(file="./redpiecesontile/67.png").subsample(2,2)
        self.tileRed68 = tk.PhotoImage(file="./redpiecesontile/68.png").subsample(2,2)
        self.tileRed69 = tk.PhotoImage(file="./redpiecesontile/69.png").subsample(2,2)
        self.tileRed70 = tk.PhotoImage(file="./redpiecesontile/70.png").subsample(2,2)
        self.tileRed71 = tk.PhotoImage(file="./redpiecesontile/71.png").subsample(2,2)
        self.tileRed72 = tk.PhotoImage(file="./redpiecesontile/72.png").subsample(2,2)
        self.tileRed73 = tk.PhotoImage(file="./redpiecesontile/73.png").subsample(2,2)
        self.tileRed74 = tk.PhotoImage(file="./redpiecesontile/74.png").subsample(2,2)
        self.tileRed75 = tk.PhotoImage(file="./redpiecesontile/75.png").subsample(2,2)
        self.tileRed76 = tk.PhotoImage(file="./redpiecesontile/76.png").subsample(2,2)
        self.tileRed77 = tk.PhotoImage(file="./redpiecesontile/77.png").subsample(2,2)
        self.tileRed78 = tk.PhotoImage(file="./redpiecesontile/78.png").subsample(2,2)
        self.tileRed79 = tk.PhotoImage(file="./redpiecesontile/79.png").subsample(2,2)
        self.tileRed80 = tk.PhotoImage(file="./redpiecesontile/80.png").subsample(2,2)
        self.tileRed81 = tk.PhotoImage(file="./redpiecesontile/81.png").subsample(2,2)
        self.tileRed82 = tk.PhotoImage(file="./redpiecesontile/82.png").subsample(2,2)
        self.tileRed83 = tk.PhotoImage(file="./redpiecesontile/83.png").subsample(2,2)
        self.tileRed84 = tk.PhotoImage(file="./redpiecesontile/84.png").subsample(2,2)
        self.tileRed85 = tk.PhotoImage(file="./redpiecesontile/85.png").subsample(2,2)
        self.tileRed86 = tk.PhotoImage(file="./redpiecesontile/86.png").subsample(2,2)
        self.tileRed87 = tk.PhotoImage(file="./redpiecesontile/87.png").subsample(2,2)
        self.tileRed88 = tk.PhotoImage(file="./redpiecesontile/88.png").subsample(2,2)
        self.tileRed89 = tk.PhotoImage(file="./redpiecesontile/89.png").subsample(2,2)
        self.tileRed90 = tk.PhotoImage(file="./redpiecesontile/90.png").subsample(2,2)
        self.tileRed91 = tk.PhotoImage(file="./redpiecesontile/91.png").subsample(2,2)
        self.tileRed92 = tk.PhotoImage(file="./redpiecesontile/92.png").subsample(2,2)
        self.tileRed93 = tk.PhotoImage(file="./redpiecesontile/93.png").subsample(2,2)
        self.tileRed94 = tk.PhotoImage(file="./redpiecesontile/94.png").subsample(2,2)
        self.tileRed95 = tk.PhotoImage(file="./redpiecesontile/95.png").subsample(2,2)
        self.tileRed96 = tk.PhotoImage(file="./redpiecesontile/96.png").subsample(2,2)
        self.tileRed97 = tk.PhotoImage(file="./redpiecesontile/97.png").subsample(2,2)
        self.tileRed98 = tk.PhotoImage(file="./redpiecesontile/98.png").subsample(2,2)
        self.tileRed99 = tk.PhotoImage(file="./redpiecesontile/99.png").subsample(2,2)
        self.tileRed100 = tk.PhotoImage(file="./redpiecesontile/100.png").subsample(2,2)

        # Player 2 (Blue)
        self.tileBlue1 = tk.PhotoImage(file="./bluepiecesontile/1.png").subsample(2,2)
        self.tileBlue2 = tk.PhotoImage(file="./bluepiecesontile/2.png").subsample(2,2)
        self.tileBlue3 = tk.PhotoImage(file="./bluepiecesontile/3.png").subsample(2,2)
        self.tileBlue4 = tk.PhotoImage(file="./bluepiecesontile/4.png").subsample(2,2)
        self.tileBlue5 = tk.PhotoImage(file="./bluepiecesontile/5.png").subsample(2,2)
        self.tileBlue6 = tk.PhotoImage(file="./bluepiecesontile/6.png").subsample(2,2)
        self.tileBlue7 = tk.PhotoImage(file="./bluepiecesontile/7.png").subsample(2,2)
        self.tileBlue8 = tk.PhotoImage(file="./bluepiecesontile/8.png").subsample(2,2)
        self.tileBlue9 = tk.PhotoImage(file="./bluepiecesontile/9.png").subsample(2,2)
        self.tileBlue10 = tk.PhotoImage(file="./bluepiecesontile/10.png").subsample(2,2)
        self.tileBlue11 = tk.PhotoImage(file="./bluepiecesontile/11.png").subsample(2,2)
        self.tileBlue12 = tk.PhotoImage(file="./bluepiecesontile/12.png").subsample(2,2)
        self.tileBlue13 = tk.PhotoImage(file="./bluepiecesontile/13.png").subsample(2,2)
        self.tileBlue14 = tk.PhotoImage(file="./bluepiecesontile/14.png").subsample(2,2)
        self.tileBlue15 = tk.PhotoImage(file="./bluepiecesontile/15.png").subsample(2,2)
        self.tileBlue16 = tk.PhotoImage(file="./bluepiecesontile/16.png").subsample(2,2)
        self.tileBlue17 = tk.PhotoImage(file="./bluepiecesontile/17.png").subsample(2,2)
        self.tileBlue18 = tk.PhotoImage(file="./bluepiecesontile/18.png").subsample(2,2)
        self.tileBlue19 = tk.PhotoImage(file="./bluepiecesontile/19.png").subsample(2,2)
        self.tileBlue20 = tk.PhotoImage(file="./bluepiecesontile/20.png").subsample(2,2)
        self.tileBlue21 = tk.PhotoImage(file="./bluepiecesontile/21.png").subsample(2,2)
        self.tileBlue22 = tk.PhotoImage(file="./bluepiecesontile/22.png").subsample(2,2)
        self.tileBlue23 = tk.PhotoImage(file="./bluepiecesontile/23.png").subsample(2,2)
        self.tileBlue24 = tk.PhotoImage(file="./bluepiecesontile/24.png").subsample(2,2)
        self.tileBlue25 = tk.PhotoImage(file="./bluepiecesontile/25.png").subsample(2,2)
        self.tileBlue26 = tk.PhotoImage(file="./bluepiecesontile/26.png").subsample(2,2)
        self.tileBlue27 = tk.PhotoImage(file="./bluepiecesontile/27.png").subsample(2,2)
        self.tileBlue28 = tk.PhotoImage(file="./bluepiecesontile/28.png").subsample(2,2)
        self.tileBlue29 = tk.PhotoImage(file="./bluepiecesontile/29.png").subsample(2,2)
        self.tileBlue30 = tk.PhotoImage(file="./bluepiecesontile/30.png").subsample(2,2)
        self.tileBlue31 = tk.PhotoImage(file="./bluepiecesontile/31.png").subsample(2,2)
        self.tileBlue32 = tk.PhotoImage(file="./bluepiecesontile/32.png").subsample(2,2)
        self.tileBlue33 = tk.PhotoImage(file="./bluepiecesontile/33.png").subsample(2,2)
        self.tileBlue34 = tk.PhotoImage(file="./bluepiecesontile/34.png").subsample(2,2)
        self.tileBlue35 = tk.PhotoImage(file="./bluepiecesontile/35.png").subsample(2,2)
        self.tileBlue36 = tk.PhotoImage(file="./bluepiecesontile/36.png").subsample(2,2)
        self.tileBlue37 = tk.PhotoImage(file="./bluepiecesontile/37.png").subsample(2,2)
        self.tileBlue38 = tk.PhotoImage(file="./bluepiecesontile/38.png").subsample(2,2)
        self.tileBlue39 = tk.PhotoImage(file="./bluepiecesontile/39.png").subsample(2,2)
        self.tileBlue40 = tk.PhotoImage(file="./bluepiecesontile/40.png").subsample(2,2)
        self.tileBlue41 = tk.PhotoImage(file="./bluepiecesontile/41.png").subsample(2,2)
        self.tileBlue42 = tk.PhotoImage(file="./bluepiecesontile/42.png").subsample(2,2)
        self.tileBlue43 = tk.PhotoImage(file="./bluepiecesontile/43.png").subsample(2,2)
        self.tileBlue44 = tk.PhotoImage(file="./bluepiecesontile/44.png").subsample(2,2)
        self.tileBlue45 = tk.PhotoImage(file="./bluepiecesontile/45.png").subsample(2,2)
        self.tileBlue46 = tk.PhotoImage(file="./bluepiecesontile/46.png").subsample(2,2)
        self.tileBlue47 = tk.PhotoImage(file="./bluepiecesontile/47.png").subsample(2,2)
        self.tileBlue48 = tk.PhotoImage(file="./bluepiecesontile/48.png").subsample(2,2)
        self.tileBlue49 = tk.PhotoImage(file="./bluepiecesontile/49.png").subsample(2,2)
        self.tileBlue50 = tk.PhotoImage(file="./bluepiecesontile/50.png").subsample(2,2)
        self.tileBlue51 = tk.PhotoImage(file="./bluepiecesontile/51.png").subsample(2,2)
        self.tileBlue52 = tk.PhotoImage(file="./bluepiecesontile/52.png").subsample(2,2)
        self.tileBlue53 = tk.PhotoImage(file="./bluepiecesontile/53.png").subsample(2,2)
        self.tileBlue54 = tk.PhotoImage(file="./bluepiecesontile/54.png").subsample(2,2)
        self.tileBlue55 = tk.PhotoImage(file="./bluepiecesontile/55.png").subsample(2,2)
        self.tileBlue56 = tk.PhotoImage(file="./bluepiecesontile/56.png").subsample(2,2)
        self.tileBlue57 = tk.PhotoImage(file="./bluepiecesontile/57.png").subsample(2,2)
        self.tileBlue58 = tk.PhotoImage(file="./bluepiecesontile/58.png").subsample(2,2)
        self.tileBlue59 = tk.PhotoImage(file="./bluepiecesontile/59.png").subsample(2,2)
        self.tileBlue60 = tk.PhotoImage(file="./bluepiecesontile/60.png").subsample(2,2)
        self.tileBlue61 = tk.PhotoImage(file="./bluepiecesontile/61.png").subsample(2,2)
        self.tileBlue62 = tk.PhotoImage(file="./bluepiecesontile/62.png").subsample(2,2)
        self.tileBlue63 = tk.PhotoImage(file="./bluepiecesontile/63.png").subsample(2,2)
        self.tileBlue64 = tk.PhotoImage(file="./bluepiecesontile/64.png").subsample(2,2)
        self.tileBlue65 = tk.PhotoImage(file="./bluepiecesontile/65.png").subsample(2,2)
        self.tileBlue66 = tk.PhotoImage(file="./bluepiecesontile/66.png").subsample(2,2)
        self.tileBlue67 = tk.PhotoImage(file="./bluepiecesontile/67.png").subsample(2,2)
        self.tileBlue68 = tk.PhotoImage(file="./bluepiecesontile/68.png").subsample(2,2)
        self.tileBlue69 = tk.PhotoImage(file="./bluepiecesontile/69.png").subsample(2,2)
        self.tileBlue70 = tk.PhotoImage(file="./bluepiecesontile/70.png").subsample(2,2)
        self.tileBlue71 = tk.PhotoImage(file="./bluepiecesontile/71.png").subsample(2,2)
        self.tileBlue72 = tk.PhotoImage(file="./bluepiecesontile/72.png").subsample(2,2)
        self.tileBlue73 = tk.PhotoImage(file="./bluepiecesontile/73.png").subsample(2,2)
        self.tileBlue74 = tk.PhotoImage(file="./bluepiecesontile/74.png").subsample(2,2)
        self.tileBlue75 = tk.PhotoImage(file="./bluepiecesontile/75.png").subsample(2,2)
        self.tileBlue76 = tk.PhotoImage(file="./bluepiecesontile/76.png").subsample(2,2)
        self.tileBlue77 = tk.PhotoImage(file="./bluepiecesontile/77.png").subsample(2,2)
        self.tileBlue78 = tk.PhotoImage(file="./bluepiecesontile/78.png").subsample(2,2)
        self.tileBlue79 = tk.PhotoImage(file="./bluepiecesontile/79.png").subsample(2,2)
        self.tileBlue80 = tk.PhotoImage(file="./bluepiecesontile/80.png").subsample(2,2)
        self.tileBlue81 = tk.PhotoImage(file="./bluepiecesontile/81.png").subsample(2,2)
        self.tileBlue82 = tk.PhotoImage(file="./bluepiecesontile/82.png").subsample(2,2)
        self.tileBlue83 = tk.PhotoImage(file="./bluepiecesontile/83.png").subsample(2,2)
        self.tileBlue84 = tk.PhotoImage(file="./bluepiecesontile/84.png").subsample(2,2)
        self.tileBlue85 = tk.PhotoImage(file="./bluepiecesontile/85.png").subsample(2,2)
        self.tileBlue86 = tk.PhotoImage(file="./bluepiecesontile/86.png").subsample(2,2)
        self.tileBlue87 = tk.PhotoImage(file="./bluepiecesontile/87.png").subsample(2,2)
        self.tileBlue88 = tk.PhotoImage(file="./bluepiecesontile/88.png").subsample(2,2)
        self.tileBlue89 = tk.PhotoImage(file="./bluepiecesontile/89.png").subsample(2,2)
        self.tileBlue90 = tk.PhotoImage(file="./bluepiecesontile/90.png").subsample(2,2)
        self.tileBlue91 = tk.PhotoImage(file="./bluepiecesontile/91.png").subsample(2,2)
        self.tileBlue92 = tk.PhotoImage(file="./bluepiecesontile/92.png").subsample(2,2)
        self.tileBlue93 = tk.PhotoImage(file="./bluepiecesontile/93.png").subsample(2,2)
        self.tileBlue94 = tk.PhotoImage(file="./bluepiecesontile/94.png").subsample(2,2)
        self.tileBlue95 = tk.PhotoImage(file="./bluepiecesontile/95.png").subsample(2,2)
        self.tileBlue96 = tk.PhotoImage(file="./bluepiecesontile/96.png").subsample(2,2)
        self.tileBlue97 = tk.PhotoImage(file="./bluepiecesontile/97.png").subsample(2,2)
        self.tileBlue98 = tk.PhotoImage(file="./bluepiecesontile/98.png").subsample(2,2)
        self.tileBlue99 = tk.PhotoImage(file="./bluepiecesontile/99.png").subsample(2,2)
        self.tileBlue100 = tk.PhotoImage(file="./bluepiecesontile/100.png").subsample(2,2)

        self.tileRedAndBlue1 = tk.PhotoImage(file="./bothPiecesOnTile/1.png").subsample(2,2)
        self.tileRedAndBlue2 = tk.PhotoImage(file="./bothPiecesOnTile/2.png").subsample(2,2)
        self.tileRedAndBlue3 = tk.PhotoImage(file="./bothPiecesOnTile/3.png").subsample(2,2)
        self.tileRedAndBlue4 = tk.PhotoImage(file="./bothPiecesOnTile/4.png").subsample(2,2)
        self.tileRedAndBlue5 = tk.PhotoImage(file="./bothPiecesOnTile/5.png").subsample(2,2)
        self.tileRedAndBlue6 = tk.PhotoImage(file="./bothPiecesOnTile/6.png").subsample(2,2)
        self.tileRedAndBlue7 = tk.PhotoImage(file="./bothPiecesOnTile/7.png").subsample(2,2)
        self.tileRedAndBlue8 = tk.PhotoImage(file="./bothPiecesOnTile/8.png").subsample(2,2)
        self.tileRedAndBlue9 = tk.PhotoImage(file="./bothPiecesOnTile/9.png").subsample(2,2)
        self.tileRedAndBlue10 = tk.PhotoImage(file="./bothPiecesOnTile/10.png").subsample(2,2)
        self.tileRedAndBlue11 = tk.PhotoImage(file="./bothPiecesOnTile/11.png").subsample(2,2)
        self.tileRedAndBlue12 = tk.PhotoImage(file="./bothPiecesOnTile/12.png").subsample(2,2)
        self.tileRedAndBlue13 = tk.PhotoImage(file="./bothPiecesOnTile/13.png").subsample(2,2)
        self.tileRedAndBlue14 = tk.PhotoImage(file="./bothPiecesOnTile/14.png").subsample(2,2)
        self.tileRedAndBlue15 = tk.PhotoImage(file="./bothPiecesOnTile/15.png").subsample(2,2)
        self.tileRedAndBlue16 = tk.PhotoImage(file="./bothPiecesOnTile/16.png").subsample(2,2)
        self.tileRedAndBlue17 = tk.PhotoImage(file="./bothPiecesOnTile/17.png").subsample(2,2)
        self.tileRedAndBlue18 = tk.PhotoImage(file="./bothPiecesOnTile/18.png").subsample(2,2)
        self.tileRedAndBlue19 = tk.PhotoImage(file="./bothPiecesOnTile/19.png").subsample(2,2)
        self.tileRedAndBlue20 = tk.PhotoImage(file="./bothPiecesOnTile/20.png").subsample(2,2)
        self.tileRedAndBlue21 = tk.PhotoImage(file="./bothPiecesOnTile/21.png").subsample(2,2)
        self.tileRedAndBlue22 = tk.PhotoImage(file="./bothPiecesOnTile/22.png").subsample(2,2)
        self.tileRedAndBlue23 = tk.PhotoImage(file="./bothPiecesOnTile/23.png").subsample(2,2)
        self.tileRedAndBlue24 = tk.PhotoImage(file="./bothPiecesOnTile/24.png").subsample(2,2)
        self.tileRedAndBlue25 = tk.PhotoImage(file="./bothPiecesOnTile/25.png").subsample(2,2)
        self.tileRedAndBlue26 = tk.PhotoImage(file="./bothPiecesOnTile/26.png").subsample(2,2)
        self.tileRedAndBlue27 = tk.PhotoImage(file="./bothPiecesOnTile/27.png").subsample(2,2)
        self.tileRedAndBlue28 = tk.PhotoImage(file="./bothPiecesOnTile/28.png").subsample(2,2)
        self.tileRedAndBlue29 = tk.PhotoImage(file="./bothPiecesOnTile/29.png").subsample(2,2)
        self.tileRedAndBlue30 = tk.PhotoImage(file="./bothPiecesOnTile/30.png").subsample(2,2)
        self.tileRedAndBlue31 = tk.PhotoImage(file="./bothPiecesOnTile/31.png").subsample(2,2)
        self.tileRedAndBlue32 = tk.PhotoImage(file="./bothPiecesOnTile/32.png").subsample(2,2)
        self.tileRedAndBlue33 = tk.PhotoImage(file="./bothPiecesOnTile/33.png").subsample(2,2)
        self.tileRedAndBlue34 = tk.PhotoImage(file="./bothPiecesOnTile/34.png").subsample(2,2)
        self.tileRedAndBlue35 = tk.PhotoImage(file="./bothPiecesOnTile/35.png").subsample(2,2)
        self.tileRedAndBlue36 = tk.PhotoImage(file="./bothPiecesOnTile/36.png").subsample(2,2)
        self.tileRedAndBlue37 = tk.PhotoImage(file="./bothPiecesOnTile/37.png").subsample(2,2)
        self.tileRedAndBlue38 = tk.PhotoImage(file="./bothPiecesOnTile/38.png").subsample(2,2)
        self.tileRedAndBlue39 = tk.PhotoImage(file="./bothPiecesOnTile/39.png").subsample(2,2)
        self.tileRedAndBlue40 = tk.PhotoImage(file="./bothPiecesOnTile/40.png").subsample(2,2)
        self.tileRedAndBlue41 = tk.PhotoImage(file="./bothPiecesOnTile/41.png").subsample(2,2)
        self.tileRedAndBlue42 = tk.PhotoImage(file="./bothPiecesOnTile/42.png").subsample(2,2)
        self.tileRedAndBlue43 = tk.PhotoImage(file="./bothPiecesOnTile/43.png").subsample(2,2)
        self.tileRedAndBlue44 = tk.PhotoImage(file="./bothPiecesOnTile/44.png").subsample(2,2)
        self.tileRedAndBlue45 = tk.PhotoImage(file="./bothPiecesOnTile/45.png").subsample(2,2)
        self.tileRedAndBlue46 = tk.PhotoImage(file="./bothPiecesOnTile/46.png").subsample(2,2)
        self.tileRedAndBlue47 = tk.PhotoImage(file="./bothPiecesOnTile/47.png").subsample(2,2)
        self.tileRedAndBlue48 = tk.PhotoImage(file="./bothPiecesOnTile/48.png").subsample(2,2)
        self.tileRedAndBlue49 = tk.PhotoImage(file="./bothPiecesOnTile/49.png").subsample(2,2)
        self.tileRedAndBlue50 = tk.PhotoImage(file="./bothPiecesOnTile/50.png").subsample(2,2)
        self.tileRedAndBlue51 = tk.PhotoImage(file="./bothPiecesOnTile/51.png").subsample(2,2)
        self.tileRedAndBlue52 = tk.PhotoImage(file="./bothPiecesOnTile/52.png").subsample(2,2)
        self.tileRedAndBlue53 = tk.PhotoImage(file="./bothPiecesOnTile/53.png").subsample(2,2)
        self.tileRedAndBlue54 = tk.PhotoImage(file="./bothPiecesOnTile/54.png").subsample(2,2)
        self.tileRedAndBlue55 = tk.PhotoImage(file="./bothPiecesOnTile/55.png").subsample(2,2)
        self.tileRedAndBlue56 = tk.PhotoImage(file="./bothPiecesOnTile/56.png").subsample(2,2)
        self.tileRedAndBlue57 = tk.PhotoImage(file="./bothPiecesOnTile/57.png").subsample(2,2)
        self.tileRedAndBlue58 = tk.PhotoImage(file="./bothPiecesOnTile/58.png").subsample(2,2)
        self.tileRedAndBlue59 = tk.PhotoImage(file="./bothPiecesOnTile/59.png").subsample(2,2)
        self.tileRedAndBlue60 = tk.PhotoImage(file="./bothPiecesOnTile/60.png").subsample(2,2)
        self.tileRedAndBlue61 = tk.PhotoImage(file="./bothPiecesOnTile/61.png").subsample(2,2)
        self.tileRedAndBlue62 = tk.PhotoImage(file="./bothPiecesOnTile/62.png").subsample(2,2)
        self.tileRedAndBlue63 = tk.PhotoImage(file="./bothPiecesOnTile/63.png").subsample(2,2)
        self.tileRedAndBlue64 = tk.PhotoImage(file="./bothPiecesOnTile/64.png").subsample(2,2)
        self.tileRedAndBlue65 = tk.PhotoImage(file="./bothPiecesOnTile/65.png").subsample(2,2)
        self.tileRedAndBlue66 = tk.PhotoImage(file="./bothPiecesOnTile/66.png").subsample(2,2)
        self.tileRedAndBlue67 = tk.PhotoImage(file="./bothPiecesOnTile/67.png").subsample(2,2)
        self.tileRedAndBlue68 = tk.PhotoImage(file="./bothPiecesOnTile/68.png").subsample(2,2)
        self.tileRedAndBlue69 = tk.PhotoImage(file="./bothPiecesOnTile/69.png").subsample(2,2)
        self.tileRedAndBlue70 = tk.PhotoImage(file="./bothPiecesOnTile/70.png").subsample(2,2)
        self.tileRedAndBlue71 = tk.PhotoImage(file="./bothPiecesOnTile/71.png").subsample(2,2)
        self.tileRedAndBlue72 = tk.PhotoImage(file="./bothPiecesOnTile/72.png").subsample(2,2)
        self.tileRedAndBlue73 = tk.PhotoImage(file="./bothPiecesOnTile/73.png").subsample(2,2)
        self.tileRedAndBlue74 = tk.PhotoImage(file="./bothPiecesOnTile/74.png").subsample(2,2)
        self.tileRedAndBlue75 = tk.PhotoImage(file="./bothPiecesOnTile/75.png").subsample(2,2)
        self.tileRedAndBlue76 = tk.PhotoImage(file="./bothPiecesOnTile/76.png").subsample(2,2)
        self.tileRedAndBlue77 = tk.PhotoImage(file="./bothPiecesOnTile/77.png").subsample(2,2)
        self.tileRedAndBlue78 = tk.PhotoImage(file="./bothPiecesOnTile/78.png").subsample(2,2)
        self.tileRedAndBlue79 = tk.PhotoImage(file="./bothPiecesOnTile/79.png").subsample(2,2)
        self.tileRedAndBlue80 = tk.PhotoImage(file="./bothPiecesOnTile/80.png").subsample(2,2)
        self.tileRedAndBlue81 = tk.PhotoImage(file="./bothPiecesOnTile/81.png").subsample(2,2)
        self.tileRedAndBlue82 = tk.PhotoImage(file="./bothPiecesOnTile/82.png").subsample(2,2)
        self.tileRedAndBlue83 = tk.PhotoImage(file="./bothPiecesOnTile/83.png").subsample(2,2)
        self.tileRedAndBlue84 = tk.PhotoImage(file="./bothPiecesOnTile/84.png").subsample(2,2)
        self.tileRedAndBlue85 = tk.PhotoImage(file="./bothPiecesOnTile/85.png").subsample(2,2)
        self.tileRedAndBlue86 = tk.PhotoImage(file="./bothPiecesOnTile/86.png").subsample(2,2)
        self.tileRedAndBlue87 = tk.PhotoImage(file="./bothPiecesOnTile/87.png").subsample(2,2)
        self.tileRedAndBlue88 = tk.PhotoImage(file="./bothPiecesOnTile/88.png").subsample(2,2)
        self.tileRedAndBlue89 = tk.PhotoImage(file="./bothPiecesOnTile/89.png").subsample(2,2)
        self.tileRedAndBlue90 = tk.PhotoImage(file="./bothPiecesOnTile/90.png").subsample(2,2)
        self.tileRedAndBlue91 = tk.PhotoImage(file="./bothPiecesOnTile/91.png").subsample(2,2)
        self.tileRedAndBlue92 = tk.PhotoImage(file="./bothPiecesOnTile/92.png").subsample(2,2)
        self.tileRedAndBlue93 = tk.PhotoImage(file="./bothPiecesOnTile/93.png").subsample(2,2)
        self.tileRedAndBlue94 = tk.PhotoImage(file="./bothPiecesOnTile/94.png").subsample(2,2)
        self.tileRedAndBlue95 = tk.PhotoImage(file="./bothPiecesOnTile/95.png").subsample(2,2)
        self.tileRedAndBlue96 = tk.PhotoImage(file="./bothPiecesOnTile/96.png").subsample(2,2)
        self.tileRedAndBlue97 = tk.PhotoImage(file="./bothPiecesOnTile/97.png").subsample(2,2)
        self.tileRedAndBlue98 = tk.PhotoImage(file="./bothPiecesOnTile/98.png").subsample(2,2)
        self.tileRedAndBlue99 = tk.PhotoImage(file="./bothPiecesOnTile/99.png").subsample(2,2)
        self.tileRedAndBlue100 = tk.PhotoImage(file="./bothPiecesOnTile/100.png").subsample(2,2)


        # List containing PhotoImage variables of no players on tiles
        self.noPlayersOnTiles = [self.tile1,self.tile2,self.tile3,self.tile4,self.tile5,self.tile6,self.tile7,self.tile8,self.tile9,
                            self.tile10,self.tile11,self.tile12,self.tile13,self.tile14,self.tile15,self.tile16,self.tile17,
                            self.tile18,self.tile19,self.tile20,self.tile21,self.tile22,self.tile23,self.tile24,self.tile25,
                            self.tile26,self.tile27,self.tile28,self.tile29,self.tile30,self.tile31,self.tile32,self.tile33,
                            self.tile34,self.tile35,self.tile36,self.tile37,self.tile38,self.tile39,self.tile40,self.tile41,
                            self.tile42,self.tile43,self.tile44,self.tile45,self.tile46,self.tile47,self.tile48,self.tile49,
                            self.tile50,self.tile51,self.tile52,self.tile53,self.tile54,self.tile55,self.tile56,self.tile57,
                            self.tile58,self.tile59,self.tile60,self.tile61,self.tile62,self.tile63,self.tile64,self.tile65,
                            self.tile66,self.tile67,self.tile68,self.tile69,self.tile70,self.tile71,self.tile72,self.tile73,
                            self.tile74,self.tile75,self.tile76,self.tile77,self.tile78,self.tile79,self.tile80,self.tile81,
                            self.tile82,self.tile83,self.tile84,self.tile85,self.tile86,self.tile87,self.tile88,self.tile89,
                            self.tile90,self.tile91,self.tile92,self.tile93,self.tile94,self.tile95,self.tile96,self.tile97,
                            self.tile98,self.tile99,self.tile100,]
        # List containing PhotoImage variables of red only tiles
        self.redOnlyTiles = [self.tileRed1,self.tileRed2,self.tileRed3,self.tileRed4,self.tileRed5,self.tileRed6,self.tileRed7,
                        self.tileRed8,self.tileRed9,self.tileRed10,self.tileRed11,self.tileRed12,self.tileRed13,self.tileRed14,
                        self.tileRed15,self.tileRed16,self.tileRed17,self.tileRed18,self.tileRed19,self.tileRed20,self.tileRed21,
                        self.tileRed22,self.tileRed23,self.tileRed24,self.tileRed25,self.tileRed26,self.tileRed27,self.tileRed28,
                        self.tileRed29,self.tileRed30,self.tileRed31,self.tileRed32,self.tileRed33,self.tileRed34,self.tileRed35,
                        self.tileRed36,self.tileRed37,self.tileRed38,self.tileRed39,self.tileRed40,self.tileRed41,self.tileRed42,
                        self.tileRed43,self.tileRed44,self.tileRed45,self.tileRed46,self.tileRed47,self.tileRed48,self.tileRed49,
                        self.tileRed50,self.tileRed51,self.tileRed52,self.tileRed53,self.tileRed54,self.tileRed55,self.tileRed56,
                        self.tileRed57,self.tileRed58,self.tileRed59,self.tileRed60,self.tileRed61,self.tileRed62,self.tileRed63,
                        self.tileRed64,self.tileRed65,self.tileRed66,self.tileRed67,self.tileRed68,self.tileRed69,self.tileRed70,
                        self.tileRed71,self.tileRed72,self.tileRed73,self.tileRed74,self.tileRed75,self. tileRed76,
                        self.tileRed77,self.tileRed78,self.tileRed79,self.tileRed80,self.tileRed81,self.tileRed82,self.tileRed83,
                        self.tileRed84,self.tileRed85,self. tileRed86,self.tileRed87,self. tileRed88,self. tileRed89,
                        self.tileRed90,self.tileRed91,self.tileRed92,self.tileRed93,self.tileRed94,self.tileRed95,self.tileRed96,
                        self.tileRed97,self.tileRed98,self. tileRed99,self. tileRed100]

        # List containing PhotoImage variables of blue only tiles
        self.blueOnlyTiles = [self.tileBlue1,self.tileBlue2,self.tileBlue3,self.tileBlue4,self.tileBlue5,self.tileBlue6,
                              self.tileBlue7,self.tileBlue8,self.tileBlue9,self.tileBlue10,self.tileBlue11,self.tileBlue12,
                              self.tileBlue13,self.tileBlue14,self.tileBlue15,self.tileBlue16,self.tileBlue17,self.tileBlue18,
                              self.tileBlue19,self.tileBlue20,self.tileBlue21,self.tileBlue22,self.tileBlue23,self.tileBlue24,
                              self.tileBlue25,self.tileBlue26,self.tileBlue27,self.tileBlue28,self.tileBlue29,self.tileBlue30,
                              self.tileBlue31,self.tileBlue32,self.tileBlue33,self.tileBlue34,self.tileBlue35,self.tileBlue36,
                              self.tileBlue37,self.tileBlue38,self.tileBlue39,self.tileBlue40,self.tileBlue41,self.tileBlue42,
                              self.tileBlue43,self.tileBlue44,self.tileBlue45,self.tileBlue46,self.tileBlue47,self.tileBlue48,
                              self.tileBlue49,self.tileBlue50,self.tileBlue51,self.tileBlue52,self.tileBlue53,self.tileBlue54,
                              self.tileBlue55,self.tileBlue56,self.tileBlue57,self.tileBlue58,self.tileBlue59,self.tileBlue60,
                              self.tileBlue61,self.tileBlue62,self.tileBlue63,self.tileBlue64,self.tileBlue65,self.tileBlue66,
                              self.tileBlue67,self.tileBlue68,self.tileBlue69,self.tileBlue70,self.tileBlue71,self.tileBlue72,
                              self.tileBlue73,self.tileBlue74,self.tileBlue75,self.tileBlue76,
                              self.tileBlue77,self.tileBlue78,self.tileBlue79,self.tileBlue80,self.tileBlue81,self.tileBlue82,
                              self.tileBlue83,self.tileBlue84,self.tileBlue85,self.tileBlue86,self.tileBlue87,self.tileBlue88,
                              self.tileBlue89,self.tileBlue90,self.tileBlue91,self.tileBlue92,self.tileBlue93,self.tileBlue94,
                              self.tileBlue95,self.tileBlue96,self.tileBlue97,self.tileBlue98,self.tileBlue99,self.tileBlue100]
        # List containing PhotoImage variables of both RED and BLUE tiles
        self.redAndBlueTiles = [self.tileRedAndBlue1,self.tileRedAndBlue2,self.tileRedAndBlue3,self.tileRedAndBlue4,
                                self.tileRedAndBlue5,self.tileRedAndBlue6,self.tileRedAndBlue7,self.tileRedAndBlue8,
                                self.tileRedAndBlue9,self.tileRedAndBlue10,self.tileRedAndBlue11,self.tileRedAndBlue12,
                                self.tileRedAndBlue13,self.tileRedAndBlue14,self.tileRedAndBlue15,self.tileRedAndBlue16,
                                self.tileRedAndBlue17,self.tileRedAndBlue18,self.tileRedAndBlue19,self.tileRedAndBlue20,
                                self.tileRedAndBlue21,self.tileRedAndBlue22,self.tileRedAndBlue23,self.tileRedAndBlue24,
                                self.tileRedAndBlue25,self.tileRedAndBlue26,self.tileRedAndBlue27,self.tileRedAndBlue28,
                                self.tileRedAndBlue29,self.tileRedAndBlue30,self.tileRedAndBlue31,self.tileRedAndBlue32,
                                self.tileRedAndBlue33,self.tileRedAndBlue34,self.tileRedAndBlue35,self.tileRedAndBlue36,
                                self.tileRedAndBlue37,self.tileRedAndBlue38,self.tileRedAndBlue39,self.tileRedAndBlue40,
                                self.tileRedAndBlue41,self.tileRedAndBlue42,self.tileRedAndBlue43,self.tileRedAndBlue44,
                                self.tileRedAndBlue45,self.tileRedAndBlue46,self.tileRedAndBlue47,self.tileRedAndBlue48,
                                self.tileRedAndBlue49,self.tileRedAndBlue50,self.tileRedAndBlue51,self.tileRedAndBlue52,
                                self.tileRedAndBlue53,self.tileRedAndBlue54,self.tileRedAndBlue55,self.tileRedAndBlue56,
                                self.tileRedAndBlue57,self.tileRedAndBlue58,self.tileRedAndBlue59,self.tileRedAndBlue60,
                                self.tileRedAndBlue61,self.tileRedAndBlue62,self.tileRedAndBlue63,self.tileRedAndBlue64,
                                self.tileRedAndBlue65,self.tileRedAndBlue66,self.tileRedAndBlue67,self.tileRedAndBlue68,
                                self.tileRedAndBlue69,self.tileRedAndBlue70,self.tileRedAndBlue71,self.tileRedAndBlue72,
                                self.tileRedAndBlue73,self.tileRedAndBlue74,self.tileRedAndBlue75,self.tileRedAndBlue76,
            self.tileRedAndBlue77,self.tileRedAndBlue78,self.tileRedAndBlue79,self.tileRedAndBlue80,self.tileRedAndBlue81,
                                self.tileRedAndBlue82,self.tileRedAndBlue83,self.tileRedAndBlue84,self.tileRedAndBlue85,
                                self.tileRedAndBlue86,self.tileRedAndBlue87,self.tileRedAndBlue88,self.tileRedAndBlue89,
                                self.tileRedAndBlue90,self.tileRedAndBlue91,self.tileRedAndBlue92,self.tileRedAndBlue93,
                                self.tileRedAndBlue94,self.tileRedAndBlue95,self.tileRedAndBlue96,self.tileRedAndBlue97,
                                self.tileRedAndBlue98,self.tileRedAndBlue99,self.tileRedAndBlue100]

        self.rowMap = {0:[self.tile100,self.tile99,self.tile98,self.tile97,self.tile96,self.tile95,self.tile94,self.tile93,self.tile92,self.tile91],
          1:[self.tile81,self.tile82,self.tile83,self.tile84,self.tile85,self.tile86,self.tile87,self.tile88,self.tile89,self.tile90],
        2:[self.tile80,self.tile79,self.tile78,self.tile77,self.tile76,self.tile75,self.tile74,self.tile73,self.tile72,self.tile71],
          3:[self.tile61,self.tile62,self.tile63,self.tile64,self.tile65,self.tile66,self.tile67,self.tile68,self.tile69,self.tile70],
        4:[self.tile60,self.tile59,self.tile58,self.tile57,self.tile56,self.tile55,self.tile54,self.tile53,self.tile52,self.tile51],
          5:[self.tile41,self.tile42,self.tile43,self.tile44,self.tile45,self.tile46,self.tile47,self.tile48,self.tile49,self.tile50],
          6:[self.tile40,self.tile39,self.tile38,self.tile37,self.tile36,self.tile35,self.tile34,self.tile33,self.tile32,self.tile31],
          7:[self.tile21,self.tile22,self.tile23,self.tile24,self.tile25,self.tile26,self.tile27,self.tile28,self.tile29,self.tile30],
          8:[self.tile20,self.tile19,self.tile18,self.tile17,self.tile16,self.tile15,self.tile14,self.tile13,self.tile12,self.tile11],
          9:[self.tile1,self.tile2,self.tile3,self.tile4,self.tile5,self.tile6,self.tile7,self.tile8,self.tile9,self.tile10]
          }
        self.boardTiles = []
        for rowIndex in range(9,-1,-1):
            arr = self.rowMap.get(rowIndex)
            currentRowElements = []
            for columnIndex in range(0,10):
                button = tk.Label(self.window,image=arr[columnIndex],bd=0)
                button.grid(row=rowIndex,column=columnIndex)
                currentRowElements.append(button)
            if rowIndex%2==1:
                self.boardTiles.extend(currentRowElements)
            else:
                self.boardTiles.extend(currentRowElements[::-1])

        # Left side of frame
        self.winnerLabel = tk.Label(self.frameLeft,image=self.winnerBoardPicture,bg="#e5cbc2")
        self.winnerLabel.pack(padx=10,pady=20)
        self.player1Score = tk.Label(self.frameLeft,font=("Comic Sans",15),image=self.player1Piece,bg="#e5cbc2")
        self.player1Score.pack(padx=40)
        self.player2Score = tk.Label(self.frameLeft,font=("Comic Sans",15),image=self.player2Piece,state=tk.DISABLED,bg="#e5cbc2")
        self.player2Score.pack(padx=40)
        self.frameControls = tk.Frame(self.mainFrame,bg="black")
        self.frameControls.grid(row=1,column=1,pady=20)
        self.rollButton = tk.Button(self.frameControls,text="Roll Dice",bd=0,bg="black",font=("Helvetica",12),activebackground="black", fg="white",activeforeground="white", command=self.rollDice,image=self.diceButtonIcon,compound=tk.BOTTOM)
        self.rollButton.grid(row=0,column=0,pady=10,padx=10)
        self.display = tk.Label(self.frameControls,image=self.diceFace1,bg="black")
        self.display.grid(row=0,column=1)
        self.player1PieceOutside = tk.Label(self.root,image=self.player1PieceSmall,bg="#e5cbc2")
        self.player1PieceOutside.place(x=215,y=564)
        self.player2PieceOutside = tk.Label(self.root,image=self.player2PieceSmall,bg="#e5cbc2")
        self.player2PieceOutside.place(x=250,y=560)
        self.exitGameButton = tk.Button(self.frameRight,image=self.exitGameButtonImage,bd=0,command=self.root.destroy,bg="#e5cbc2",activebackground="#e5cbc2")
        self.exitGameButton.pack(padx=30)
        # play again
        self.startGameButton = tk.Button(self.frameRight,command=self.playGame,image=self.playAgainButtonImage,bd=0,bg="#e5cbc2",activebackground="#e5cbc2")
        self.startGameButton.pack(padx=30,pady=10)
        self.soundButton = tk.Button(self.frameRight,image=self.soundOnPicture,bd=0,command=self.changeAllSoundState,bg="#e5cbc2",activebackground="#e5cbc2")
        self.soundButton.pack(padx=30,pady=10)
        self.root.iconphoto(True,self.snakesAndLaddersIcon)
        self.playGame()
        self.root.mainloop()

    def hidePlayer1PieceOutside(self):
        self.player1PieceOutside.place_forget()

    def hidePlayer2PieceOutside(self):
        self.player2PieceOutside.place_forget()

    def showPlayer1PieceOutside(self):
        self.player1PieceOutside.place(x=215, y=564)

    def showPlayer2PieceOutside(self):
        self.player2PieceOutside.place(x=250, y=560)

    def changeAllSoundState(self):
        self.allSoundActive = not (self.allSoundActive)
        if self.allSoundActive == True:
            self.soundButton.config(image=self.soundOnPicture)
        else:
            self.soundButton.config(image=self.soundOffPicture)

    def playPlayerMovementSound(self):
        if self.allSoundActive == True:
            mixer.init()
            # Loading the sound
            mixer.music.load("mixkit-instant-win-2021.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
    def playLadderUpSound(self):
        if self.allSoundActive == True:
            mixer.init()
            mixer.music.load("mixkit-game-bonus-reached-2065.wav")
            mixer.music.set_volume(0.4)
            mixer.music.play()
    def playGameoverSound(self):
        if self.allSoundActive == True:
            mixer.init()
            mixer.music.load("game-over-160612.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()

    def playSnakeDownSound(self):
        if self.allSoundActive == True:
            mixer.init()
            # Loading the sound
            mixer.music.load("mixkit-player-losing-or-failing-2042.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()

    def threadPlayerMovementSound(self):
        audio_thread = Thread(target=self.playPlayerMovementSound)
        audio_thread.start()

    def threadPlayLadderSound(self):
        audio_thread = Thread(target=self.playLadderUpSound)
        audio_thread.start()

    def threadPlayGameoverSound(self):
        audio_thread = Thread(target=self.playGameoverSound)
        audio_thread.start()

    def threadSnakeDownSound(self):
        audio_thread = Thread(target=self.playSnakeDownSound)
        audio_thread.start()

    def playGame(self):
        self.player1Turn = True
        self.player1Score.config(state=tk.NORMAL)
        self.player2Turn = False
        self.player2Score.config(state=tk.DISABLED)
        self.boardTiles[self.player1Position - 1].config(image=self.noPlayersOnTiles[self.player1Position - 1])
        self.boardTiles[self.player2Position - 1].config(image=self.noPlayersOnTiles[self.player2Position - 1])
        self.boardTiles[self.prevPlayer1Position - 1].config(image=self.noPlayersOnTiles[self.prevPlayer1Position - 1])
        self.boardTiles[self.prevPlayer2Position - 1].config(image=self.noPlayersOnTiles[self.prevPlayer2Position - 1])
        self.player1Position = self.player2Position = 0
        self.prevPlayer1Position = self.prevPlayer2Position = 0
        self.gameOver = False
        self.activateRollDiceButton()
        self.disablePlayAgainButton()
        self.winnerLabel.config(image=self.winnerBoardPicture)
        self.showPlayer1PieceOutside()
        self.showPlayer2PieceOutside()

    def rollDice(self):
        self.threadPlayerMovementSound()
        sides = 7
        face = random.randrange(1, sides)
        self.diceRolling(face)
        if self.player1Turn == True:
            self.hidePlayer1PieceOutside()
            if (self.player1Position + face) <= 100:
                newPosition = self.player1Position + face
                # Change tile image in previous position
                if self.player1Position == self.player2Position and self.player1Position != 0:
                    self.boardTiles[self.player1Position - 1].config(image=self.blueOnlyTiles[self.player1Position - 1])
                else:
                    self.boardTiles[self.player1Position - 1].config(image=self.noPlayersOnTiles[self.player1Position - 1])
                # Reached goal. Winner
                if newPosition >= 100:
                    newPosition = 100
                    self.gameOver = True
                # checking for Ladder in the newly moving tile
                if newPosition in self.ladderMap:
                    self.threadPlayLadderSound()
                    newPosition = self.ladderMap.get(newPosition)
                elif newPosition in self.snakesMap: # checking for snake in the newly moving tile
                    self.threadSnakeDownSound()
                    newPosition = self.snakesMap.get(newPosition)
                # Change tile image in the new position
                if newPosition != self.player2Position:
                    self.boardTiles[newPosition - 1].config(image=self.redOnlyTiles[newPosition - 1])
                elif newPosition == self.player2Position:
                    self.boardTiles[newPosition - 1].config(image=self.redAndBlueTiles[newPosition - 1])
                # Assign the tile number where player1 is present as the previous player 1 position
                self.prevPlayer1Position = self.player1Position
                # change player1Position to the current tile where Player 1 is present.
                self.player1Position = newPosition
        elif self.player2Turn == True:  # BLUE
            self.hidePlayer2PieceOutside()
            if (self.player2Position + face) <= 100:
                newPosition = self.player2Position + face
                # change tile image in previous position
                if self.player2Position == self.player1Position:
                    self.boardTiles[self.player2Position - 1].config(image=self.redOnlyTiles[self.player2Position - 1])
                else:
                    self.boardTiles[self.player2Position - 1].config(image=self.noPlayersOnTiles[self.player2Position - 1])
                # Check if reached 100 or more
                if newPosition >= 100:
                    newPosition = 100
                    self.gameOver = True
                # checking for Ladder in the newly moving tile
                if newPosition in self.ladderMap:
                    self.threadPlayLadderSound()
                    newPosition = self.ladderMap.get(newPosition)
                elif newPosition in self.snakesMap: # checking for snakes in the newly moving tile
                    self.threadSnakeDownSound()
                    newPosition = self.snakesMap.get(newPosition)
                # Change tile image in the newly moving position
                if newPosition == self.player1Position:
                    self.boardTiles[newPosition - 1].config(image=self.redAndBlueTiles[newPosition - 1])
                else:
                    self.boardTiles[newPosition - 1].config(image=self.blueOnlyTiles[newPosition - 1])
                # Assign the tile number where player2 is present as the previous player 2 position
                self.prevPlayer2Position = self.player2Position
                # change player2Position to the current tile where Player 2 is present.
                self.player2Position = newPosition
        if self.gameOver == False:
            if face != 6:
                self.changeTurn()
        else:
            self.gameOverFunct()
            if self.player1Turn == True:
                self.winnerLabel.config(image=self.winnerBoardRedPicture)
                messagebox.showinfo("GAME OVER", "Player RED is Winner!")
            elif self.player2Turn == True:
                self.winnerLabel.config(image=self.winnerBoardBluePicture)
                messagebox.showinfo("GAME OVER", "Player BLUE is Winner!")

    def gameOverFunct(self):
        self.threadPlayGameoverSound()
        self.rollButton.config(state=tk.DISABLED)
        self.activatePlayAgainButton()

    def diceRolling(self,faceValue):
        if faceValue == 1:
            self.display.config(image=self.diceFace1)
        elif faceValue == 2:
            self.display.config(image=self.diceFace2)
        elif faceValue == 3:
            self.display.config(image=self.diceFace3)
        elif faceValue == 4:
            self.display.config(image=self.diceFace4)
        elif faceValue == 5:
            self.display.config(image=self.diceFace5)
        elif faceValue == 6:
            self.display.config(image=self.diceFace6)

    def disableRollDiceButton(self):
        self.rollButton.config(state=tk.DISABLED)

    def activateRollDiceButton(self):
        self.rollButton.config(state=tk.NORMAL)

    def disablePlayAgainButton(self):
        self.startGameButton.config(state=tk.DISABLED)

    def activatePlayAgainButton(self):
        self.startGameButton.config(state=tk.NORMAL)

    def changeTurn(self):
        self.player1Turn = not (self.player1Turn)
        self.player2Turn = not (self.player2Turn)
        if self.player1Turn is True:
            self.player1Score.config(state=tk.NORMAL)
        else:
            self.player1Score.config(state=tk.DISABLED)
        if self.player2Turn is True:
            self.player2Score.config(state=tk.NORMAL)
        else:
            self.player2Score.config(state=tk.DISABLED)
# Object created for the class 'SnakeAndLadder'
SnakesAndLadder()