import imgpath
from Planet import Planet

geonosis = Planet(True, 'Geonosis', (223, 119, 0), (30, 130, 40, 40), imgpath.geonosis_h_path, imgpath.geonosis_v_path, '', '')
felucia = Planet(False, 'Felucia', (137, 179, 0), (30, 180, 40, 40), imgpath.felucia_h_path, imgpath.felucia_v_path, '', '')
naboo = Planet(False, 'Naboo', (255, 225, 254), (30, 230, 40, 40), imgpath.naboo_h_path, imgpath.naboo_v_path, '', '')
endor = Planet(False, 'Endor', (4, 132, 0), (30, 280, 40, 40), imgpath.endor_h_path, imgpath.endor_v_path, '', '')
hoth = Planet(False, 'Hoth', (240, 240, 240), (30, 330, 40, 40), imgpath.hoth_h_path, imgpath.hoth_v_path, '', '')
death_star = Planet(False, 'Death star', (55, 55, 55), (30, 380, 40, 40), imgpath.death_star_h_path, imgpath.death_star_v_path, '', '')
bespin = Planet(False, 'Bespin', (255, 255, 255), (30, 430, 40, 40), imgpath.bespin_h_path, imgpath.bespin_v_path, '', '')
tatooine = Planet(False, 'Tatooine', (255, 225, 152), (30, 480, 40, 40), imgpath.tatooine_h_path, imgpath.tatooine_v_path, '', '')
scarif = Planet(False, 'Scarif', (122, 252, 243), (30, 530, 40, 40), imgpath.scarif_h_path, imgpath.scarif_v_path, '', '')
crait = Planet(False, 'Crait', (213, 213, 213), (30, 580, 40, 40), imgpath.crait_h_path, imgpath.crait_v_path, '', '')
takodana = Planet(False, 'Takodana', (175, 128, 0), (30, 630, 40, 40), imgpath.takodana_h_path, imgpath.takodana_v_path, '', '')

planets = [geonosis, felucia, naboo, endor, hoth, death_star, bespin, tatooine, scarif, crait, takodana]
