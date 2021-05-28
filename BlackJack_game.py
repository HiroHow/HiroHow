import random
import os

suits=('♦','♥','♣','♠')
ranks = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
# 创建牌的初始花色以及牌的数值并且定义每个牌的数值
cards_value ={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11 or 1}
print("Welcom to the world of Black Jack, try you best of winning point in 21 and if exceed this number will be bust!")
Basic = input('Do you want to play:')
if Basic[0].lower() == "y":
    playing = True
    ask = input('how many chips did you brint today:')
else:
    playing = False
    print('Welcome back')
    os._exit(0)

    


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    # 将牌的数值从类变量变为实例变量的值
    def __str__(self):
        return self.suit+ self.rank
    #当要求打印的时候返回例如：♦2 等数值
class Deck():
    def __init__(self):
        self.deck = []
        #从空白数值开始
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                #将数值存储在空白的列表里面
            
    def __str__(self):
        deck_comp = ''
        #列表初始为空白输出数值
        for card in self.deck:
            deck_comp += '\n'+card.__str__()
            #将牌里面的空白数值加入到空白输出里
        return 'The deck has: '+ deck_comp +'\n' +'total card number is: '+ str(len(self.deck))

    def shuffle(self):
        random.shuffle(self.deck)
        #将列表里面的数全部打乱
    def deal(self):
       single_card = self.deck.pop()
       #从列表里面抽出一张卡，并且从列表里面将这张卡删除而且返回它的值,类似于发卡系统
       return single_card

class Hand():
    # 是庄家和玩家的手牌系统
    def __init__(self):
        self.cards = []
        #自身的手牌数量从0开始
        self.value = 0
        # 自身手牌的总值也是从0开始
        self.aces = 0
        # 手上的A的数量也从0开始
    def add_card(self,card):
        self.cards.append(card)
        self.value += cards_value[card.rank]
        if card.rank == 'A':
            self.aces +=1 
        # 如果抽到的牌里面有A的话，则加1
    def value_for_ace(self):
        while self.value > 21 and self.aces >= 1:
            self.value -=10 
            self.aces -=1 
        # 如果有A并且已经超过21点的情况下然后还继续要牌的话，数值减去10

class Chips():
    def __init__(self):
        # self.total = int(input('How many chips that you have for today:')   
        self.total = 0
        self.total = int(ask)
        # print(self.total)     
        self.bet = 0
    def win_sit(self):
        self.total += self.bet
    def lose_sit(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips you are down for this game:'))
        except ValueError:
            print('Sorry, the bet must be a number')
        # try/except 是python的异常处理语句，在程序运行发生特定错误的时候跳过python的默认异常处理行为而跳到try处理器，并且重新执行
        else:
            if chips.bet > chips.total:
                print('sorry, you dont have enough chips,the value you have is ', chips.total)
            else:
                break
            # 如果客人下注的数额高于他所携带的数值的话报错，没有的话，跳出这个while循环

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.value_for_ace()

def hit_or_stand(deck,hand):
    global Playing
    while True:
        x = input ("Would you like to hit or stnd? Enter 'h' or 's'")
        if x[0].lower() =='h':
            # x[0].lower 的作用是无论玩家输入的是什么都能完整的识别出来
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('player stands. Dealer continuing')
            Playing = False
        else:
            print('Huh? please try again')
            continue
        break

def show_some(player,dealer):
    print("\nDealer's hand:")
    print('',dealer.cards[0])
    print('<card hidden>')
    print("\nplayer's hand:", *player.cards,sep='\n')
    # *player's card代表的是输出全部变量，然后sep 是代表的是seprate的功能

def show_all (player,dealer):
    print("\nDealer's hand:",*dealer.cards,sep='\n')
    print("Deal's hand=", dealer.value)
    print("\nPlayer's hand: ",*player.cards,sep='\n')
    print("player's hand=",player.value)

def player_busts(player,dealer,chips):
    print('Player LOSE!')
    chips.lose_sit()
def player_win(player,dealer,chips):
    print('Player WIN!')
    chips.win_sit()
def dealer_busts(player,dealer,chips):
    print('Dealer LOSE!')
    chips.win_sit()
def dealer_win(player,dealer,chips):
    print('Dealer WIN')
    chips.lose_sit()
def push(player,dealer):
    print("Dealer and Player tie! Return chips")

while True:
    # 开始调用实例变量
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    # 将牌的数值储存在依次的对象当中

    player_chips = Chips()

    take_bet(player_chips)
    print('The earn or lose for this game will be: ',int(player_chips.bet)*2)
    # 过问玩家想要下注多少
    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value >21:
            show_all(player_hand,dealer_hand)
            player_busts(player_hand,dealer_hand,player_chips)
            # 在player__busts的情况下recall hand的function
            break
        if player_hand.value<21:
            while dealer_hand.value<18:
                hit_or_stand(deck,player_hand) 
                hit(deck,dealer_hand)
            if dealer_hand.value >21:
                show_all(player_hand,dealer_hand)
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                show_all(player_hand,dealer_hand)
                player_win(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value or (dealer_hand.value == 21 and dealer_hand.value!= player_hand):
                show_all(player_hand,dealer_hand)
                dealer_win(player_hand,dealer_hand,player_chips)
            else:
                show_all(player_hand,dealer_hand)
                push(player_hand,dealer_hand)
        # 提醒还有多少chips可以下注
        print("\n player's remaining chips is ",player_chips.total)
        break
        # 询问是否要重新开始游戏
    new_game = input("would you like to play again? Enter 'Yes' or 'No' ")
    if new_game[0].lower() =='y':
        playing = True
        continue
    else:
        a= player_chips.total - int(ask)
        print('nice to have you and you total earning today is: ', a)
        break


