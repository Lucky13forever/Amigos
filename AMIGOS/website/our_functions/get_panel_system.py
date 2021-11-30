def get_panel_system(all_panels,user_buget,user_length,user_width):
    max_total_power=0
    total_price=0
    number_of_panels=0
    index_panel=-1
    for i in range(len(all_panels)):
        if ((all_panels[i].length<=user_length and all_panels[i].width<=user_width) or (all_panels[i].width<=user_length and all_panels[i].length<=user_width)):
            if user_length//all_panels[i].length*user_width//all_panels[i].width>user_length//all_panels[i].width*user_width//all_panels[i].length:
                max_number_of_panel=user_length//all_panels[i].length*user_width//all_panels[i].width
            else:
                max_number_of_panel=user_length//all_panels[i].width*user_width//all_panels[i].length
            contor=0
            current_price=0
            current_power=0
            while contor<=max_number_of_panel and current_price+all_panels[i].price<=user_buget:
                contor+=1
                current_price+=all_panels[i].price
                current_power+=all_panels[i].power
            if (current_power>max_total_power) or (current_power==max_total_power and current_price<total_price):
                max_total_power=current_power
                total_price=current_price
                number_of_panels=contor
                index_panel=i
    if index_panel!=-1:
        return (all_panels[index_panel],number_of_panels,max_total_power,total_price)
    return None

# Eduard Soreata , Iulia Popa



