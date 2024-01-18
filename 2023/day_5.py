from pathlib import Path

text = []
program_fp = Path(__file__)
data_fp = program_fp.parent / f"{program_fp.stem}.txt"

def parse_in_map(start_line:int, end_line: int, text: list[str]):
    return [tuple(map(int,text[start_line-1+i].split())) for i in range(end_line-start_line+1)]

with open(data_fp, "r", encoding="utf-8") as file:
    text = [line.strip() for line in file]
    seeds_l = list(map(int,text[0][7:].split(" ")))
    seed_to_soil_map =  [tuple(map(int,text[3+i].split())) for i in range(20)]
    soil_to_fert_map =  [tuple(map(int,text[25+i].split())) for i in range(28)]
    fert_to_water_map =  [tuple(map(int,text[55+i].split())) for i in range(32)]
    water_to_light_map =  parse_in_map(90, 121, text)
    light_to_temp_map = parse_in_map(124, 166, text)
    temp_to_humid = parse_in_map(169, 202, text)
    humid_to_loc = parse_in_map(205, 219, text)
    
    
def part_1(seeds_l, seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc):

    big_l = [seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc]
    run = seeds_l
    cop = []
    for change in big_l:
        for seed in run:
            # 98 50 2; 98: 50, 99: 51 
            put_in_seed = False
            for dest, src, step in change:
                if src <= seed < src + step:
                    # in range
                    cop.append(dest + (seed-src))
                    put_in_seed = True
            if not put_in_seed:
                cop.append(seed)
        run = cop.copy()
        cop.clear()
        
    return min(run)

def part_2(seeds_l, seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc):
    big_l = [seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc]
    starts_ranges = [seeds_l[x:x+2] for x in range(0, len(seeds_l))]
    # for st_seed, rang in starts_ranges:
    #     end_seed = st_seed + rang-1
        
    #     if src <= st_seed < src + step:
        
    run = starts_ranges
    cop = []
    for change in big_l:
        for st_seed, rang in run:
            # 98 50 2; 98: 50, 99: 51 
            for dest, src, step in change:
                # if our seed start is in the range of the map
                if src <= st_seed < src + step:
                    # in range
                    new_start = dest + st_seed-src
                    # we know st_seed is less than src + step but st_seed+rang could be bigger
                    change_end = src+step
                    seed_end = st_seed + rang 
                    new_end = min(seed_end, change_end)
                    new_step = (new_end - new_start) +1
                    cop.append((new_start, new_step))

                # if our map start is in the range of seeds
                elif st_seed <= src < st_seed + rang:
                    # in range
                    offset = src-st_seed
                    new_start = dest + offset
                    
                    temp_end = min(st_seed+rang-1, src+step-1)
                    new_range = temp_end - src + 1
                     
                    # we know st_seed is less than src + step but st_seed+rang could be bigger
                    cop.append((new_start, new_range))

        run = cop.copy()
        cop.clear()
    

print(f"{part_1(seeds_l, seed_to_soil_map, soil_to_fert_map, fert_to_water_map, water_to_light_map, light_to_temp_map, temp_to_humid, humid_to_loc)}")
# print(f"{part_2(seeds_l, seed_to_soil_map, soil_to_fert_map, fert_to_water_map, water_to_light_map, light_to_temp_map, temp_to_humid, humid_to_loc)}")
