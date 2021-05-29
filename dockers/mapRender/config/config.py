import os

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/{}".format(poi['EntityId'])
        return "Last known location for {}".format(poi['EntityId'])

def signFilter(poi):
    import os
    if poi['id'] in ['Sign', 'minecraft:sign']:
        sign_filter = os.environ['RENDER_SIGNS_FILTER']
        hide_filter = os.environ['RENDER_SIGNS_HIDE_FILTER'] == 'true'
        lines = list(map(lambda l: l.strip(), [poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']]))
        while lines and not lines[0]:
            del lines[0]
        while lines and not lines[-1]:
            del lines[-1]
        render_all_signs = len(sign_filter) == 0
        render_this_sign = sign_filter in lines
        if render_all_signs or render_this_sign:
            if hide_filter and not render_all_signs:
                lines = list(filter(lambda l: l != sign_filter, lines))
            return os.environ['RENDER_SIGNS_JOINER'].join(lines)

worlds["Daedalus"] = "/home/minecraft/server/world"
worlds["Daedalus Nether"] = "/home/minecraft/server/world_nether"
worlds["Daedalus End"] = "/home/minecraft/server/world_the_end"

worlds["Cerberus"] = "/home/minecraft/spigot/world"
worlds["Cerberus Nether"] = "/home/minecraft/spigot/world_nether"
worlds["Cerberus End"] = "/home/minecraft/spigot/world_the_end"

markers = [
    dict(name="Player", filterFunction=playerIcons, checked=True),
    dict(name="Sign", filterFunction=signFilter, checked=True)
    #dict(name="Towns", filterFunction=townFilter, icon="icons/marker_town.png", checked=True)
]

## Daedalus
renders["Daedalus day"] = {
    "world": "Daedalus",
    "title": "Daedalus Day",
    "rendermode": "smooth_lighting",
    "dimension": "overworld",
    "markers": markers
}
renders["Daedalus overlay_biome"] = {
    "world": "Daedalus",
    "title": "Biome Coloring Overlay",
    "rendermode": [ClearBase(), BiomeOverlay()],
    "dimension": "overworld",
    "overlay": ["Daedalus day"]
}
renders["Daedalus overlay_mobs"] = {
    "world": "Daedalus",
    "title": "Mob Spawnable Areas Overlay",
    "rendermode": [ClearBase(), SpawnOverlay()],
    "dimension": "overworld",
    "overlay": ["Daedalus day"]
}
renders["Daedalus overlay_slime"] = {
    "world": "Daedalus",
    "title": "Slime Chunk Overlay",
    "rendermode": [ClearBase(), SlimeOverlay()],
    "dimension": "overworld",
    "overlay": ["Daedalus day"]
}
renders["Daedalus night"] = {
    "world": "Daedalus",
    "title": "Daedalus Night",
    "rendermode": "smooth_night",
    "dimension": "overworld",
    "markers": markers
}
renders["Daedalus cave"] = {
    "world": "Daedalus",
    "title": "Daedalus Cave",
    "rendermode": "cave",
    "dimension": "overworld",
    "markers": markers
}

renders["Daedalus nether light"] = {
    "world": "Daedalus Nether",
    "title": "Daedalus Nether Light",
    "rendermode": "nether",
    "dimension": "nether",
    "markers": markers
}
renders["Daedalus nether dark"] = {
    "world": "Daedalus Nether",
    "title": "Daedalus Nether Dark",
    "rendermode": "nether_smooth_lighting",
    "dimension": "nether",
    "markers": markers
}
renders["Daedalus overlay_biome nether"] = {
    "world": "Daedalus Nether",
    "title": "Biome Coloring Overlay",
    "rendermode": [ClearBase(), BiomeOverlay()],
    "dimension": "nether",
    "overlay": ["Daedalus nether light"]
}

renders["Daedalus End"] = {
    "world": "Daedalus End",
    "title": "Daedalus End",
    "rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.5)],
    "dimension": "end",
    "markers": markers
}

## Cerberus
renders["Cerberus day"] = {
    "world": "Cerberus",
    "title": "Cerberus Day",
    "rendermode": "smooth_lighting",
    "dimension": "overworld",
    "markers": markers
}
renders["Cerberus overlay_biome"] = {
    "world": "Cerberus",
    "title": "Biome Coloring Overlay",
    "rendermode": [ClearBase(), BiomeOverlay()],
    "dimension": "overworld",
    "overlay": ["Cerberus day"]
}
renders["Cerberus overlay_mobs"] = {
    "world": "Cerberus",
    "title": "Mob Spawnable Areas Overlay",
    "rendermode": [ClearBase(), SpawnOverlay()],
    "dimension": "overworld",
    "overlay": ["Cerberus day"]
}
renders["Cerberus overlay_slime"] = {
    "world": "Cerberus",
    "title": "Slime Chunk Overlay",
    "rendermode": [ClearBase(), SlimeOverlay()],
    "dimension": "overworld",
    "overlay": ["Cerberus day"]
}
renders["Cerberus night"] = {
    "world": "Cerberus",
    "title": "Cerberus Night",
    "rendermode": "smooth_night",
    "dimension": "overworld",
    "markers": markers
}
renders["Cerberus cave"] = {
    "world": "Cerberus",
    "title": "Cerberus Cave",
    "rendermode": "cave",
    "dimension": "overworld",
    "markers": markers
}

renders["Cerberus nether light"] = {
    "world": "Cerberus Nether",
    "title": "Cerberus Nether Light",
    "rendermode": "nether",
    "dimension": "nether",
    "markers": markers
}
renders["Cerberus nether dark"] = {
    "world": "Cerberus Nether",
    "title": "Cerberus Nether Dark",
    "rendermode": "nether_smooth_lighting",
    "dimension": "nether",
    "markers": markers
}
renders["Cerberus overlay_biome nether"] = {
    "world": "Cerberus Nether",
    "title": "Biome Coloring Overlay",
    "rendermode": [ClearBase(), BiomeOverlay()],
    "dimension": "nether",
    "overlay": ["Cerberus nether light"]
}

renders["Cerberus End"] = {
    "world": "Cerberus End",
    "title": "Cerberus End",
    "rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.5)],
    "dimension": "end",
    "markers": markers
}

outputdir = "/home/minecraft/render"