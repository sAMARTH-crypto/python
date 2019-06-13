#nested list


gamers = ['epic is bot',['wells is bot',['shaggy is bot',['alpha is gawd']]]]

def gawd_bot(the_list):

    
    for pro_bot in the_list:
        if isinstance(pro_bot,list):
            gawd_bot(pro_bot)
        else:
            print(pro_bot)


gawd_bot(gamers)