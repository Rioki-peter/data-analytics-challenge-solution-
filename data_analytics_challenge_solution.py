import json
import requests

url = 'https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json'

def get(url):
    response = requests.get(url)
    return json.loads(response.content)

response = get(url)

def functional_water_points(response):
    functioning_water_points = 0
    not_functioning_water_points = 0
    for f in response:
        if f['water_functioning'] == 'yes':
            functioning_water_points += 1
        elif f['water_functioning'] == 'no':
            not_functioning_water_points += 1
    return functioning_water_points


def communities(response):
    community_list=[]
    for r in response:
        community_list.append(r["communities_villages"])

    new_community_list = list(set(community_list))
    return new_community_list



def number_water_points_per_community(response,community_name):
    c = 0
    water_points_per_community = []
    while c < len(community_name):
        community_water_points = 0
        for i in response:
            for j in i:
                if j == 'communities_villages':
                    if i[j] == community_name[c]:
                        community_water_points += 1
                    else:
                        break;
        water_points = community_name[c],community_water_points
        water_points_per_community.append(water_points)    
        c += 1
    return water_points_per_community
                    
              

def broken_per_community(response,community_name):
    c = 0
    broken_water_points_per_community = []
    broken_water_points_per_community_percentage_List = []
    while c < len(community_name):
        broken_community_water_points = 0
        for i in response:
            for j in i:
                if j == 'water_point_condition':
                    if i[j] == 'broken':
                        continue;
                    else:
                        break;
                if j == 'communities_villages':
                    if i[j] == community_name[c]:
                        broken_community_water_points += 1
                    else:
                        break;
        broken_water_points = community_name[c],broken_community_water_points
        broken_water_points_per_community.append(broken_water_points)
        total_water_points_per_community = number_water_points_per_community(response,community_name)

        for t in total_water_points_per_community:
            if t[0] == community_name[c]:
                broken = (broken_water_points[1]/t[1])
                percentage_broken = broken * 100
                broken_water_points_per_community_percentage = (t[0],str(percentage_broken) + '%')
                broken_water_points_per_community_percentage_List.append(broken_water_points_per_community_percentage)
                break;
            
        c += 1
    return broken_water_points_per_community_percentage_List

def solution_dictionary():
    number_functional = functional_water_points(response)
    community_name = communities(response)
    number_water_points = number_water_points_per_community(response,community_name)
    community_ranking = broken_per_community(response,community_name)

    solution = {}
    solution['number_functional'] = number_functional
    solution['number_water_points'] = number_water_points
    solution['community_ranking'] = community_ranking
    return solution 



if __name__ == '__main__':
    solution = solution_dictionary()
    print (solution)



