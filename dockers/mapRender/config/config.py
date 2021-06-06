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
worlds["Daedalus Faraway Lands"] = "/home/minecraft/server/world"
worlds["Daedalus Nether"] = "/home/minecraft/server/world_nether"
worlds["Daedalus End"] = "/home/minecraft/server/world_the_end"

worlds["Cerberus"] = "/home/minecraft/spigot/world"
worlds["Cerberus Nether"] = "/home/minecraft/spigot/world_nether"
worlds["Cerberus End"] = "/home/minecraft/spigot/world_the_end"

markers = [
    dict(name="Player", filterFunction=playerIcons, checked=True),
    dict(name="Sign", filterFunction=signFilter, checked=True)
]

## Daedalus
renders["Daedalus_day"] = {
    "world": "Daedalus",
    "title": "Daedalus Day",
    "rendermode": "smooth_lighting",
    "dimension": "overworld",
    "crop": (-30000, -30000, 30000, 30000),
    "markers": markers
}
renders["Daedalus_night"] = {
    "world": "Daedalus",
    "title": "Daedalus Night",
    "rendermode": "smooth_night",
    "dimension": "overworld",
    "crop": (-30000, -30000, 30000, 30000),
    "markers": markers
}
renders["Daedalus_cave"] = {
    "world": "Daedalus",
    "title": "Daedalus Cave",
    "rendermode": "cave",
    "dimension": "overworld",
    "crop": (-30000, -30000, 30000, 30000),
    "markers": markers
}

renders["Daedalus_faraway_lands_day"] = {
    "world": "Daedalus Faraway Lands",
    "title": "Daedalus Faraway Lands Day",
    "rendermode": "smooth_lighting",
    "dimension": "overworld",
    "crop": (29970000, 29970000, 30000000, 30000000),
    "markers": markers
}
renders["Daedalus_faraway_lands_night"] = {
    "world": "Daedalus Faraway Lands",
    "title": "Daedalus Faraway Lands Night",
    "rendermode": "smooth_night",
    "dimension": "overworld",
    "crop": (29970000, 29970000, 30000000, 30000000),
    "markers": markers
}
renders["Daedalus_faraway_lands_cave"] = {
    "world": "Daedalus Faraway Lands",
    "title": "Daedalus Faraway Lands Cave",
    "rendermode": "cave",
    "dimension": "overworld",
    "crop": (29970000, 29970000, 30000000, 30000000),
    "markers": markers
}

renders["Daedalus_nether_light"] = {
    "world": "Daedalus Nether",
    "title": "Daedalus Nether Light",
    "rendermode": "nether",
    "dimension": "nether",
    "crop": (-30000, -30000, 30000, 30000),
    "markers": markers
}
renders["Daedalus_nether_dark"] = {
    "world": "Daedalus Nether",
    "title": "Daedalus Nether Dark",
    "rendermode": "nether_smooth_lighting",
    "dimension": "nether",
    "crop": (-30000, -30000, 30000, 30000),
    "markers": markers
}

renders["Daedalus_end"] = {
    "world": "Daedalus End",
    "title": "Daedalus End",
    "rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.5)],
    "dimension": "end",
    "crop": (-30000, -30000, 30000, 30000),
    "markers": markers
}

## Cerberus
renders["Cerberus_day"] = {
    "world": "Cerberus",
    "title": "Cerberus Day",
    "rendermode": "smooth_lighting",
    "dimension": "overworld",
    "crop": (-30000, -30000, 30000, 30000),
    "markers": markers
}
renders["Cerberus_night"] = {
    "world": "Cerberus",
    "title": "Cerberus Night",
    "rendermode": "smooth_night",
    "dimension": "overworld",
    "crop": (-30000, -30000, 30000, 30000),
    "markers": markers
}
renders["Cerberus_cave"] = {
    "world": "Cerberus",
    "title": "Cerberus Cave",
    "rendermode": "cave",
    "dimension": "overworld",
    "crop": (-30000, -30000, 30000, 30000),
    "markers": markers
}

renders["Cerberus_nether_light"] = {
    "world": "Cerberus Nether",
    "title": "Cerberus Nether Light",
    "rendermode": "nether",
    "dimension": "nether",
    "crop": (-30000, -30000, 30000, 30000),
    "markers": markers
}
renders["Cerberus_nether_dark"] = {
    "world": "Cerberus Nether",
    "title": "Cerberus Nether Dark",
    "rendermode": "nether_smooth_lighting",
    "dimension": "nether",
    "crop": (-30000, -30000, 30000, 30000),
    "markers": markers
}

renders["Cerberus_end"] = {
    "world": "Cerberus End",
    "title": "Cerberus End",
    "rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.5)],
    "dimension": "end",
    "crop": (-30000, -30000, 30000, 30000),
    "markers": markers
}

outputdir = "/home/minecraft/render"