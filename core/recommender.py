def generate_recommendation(insights) :
 insights = {
  "top_style": "casual",
  "top_size": "M",
  "top_shoe_size": 6
}
 style = insights["top_style"]
 size = insights["top_size"]
 shoe_size = insights['top_shoe_size']
 recommendation = (f'focus on  {style} style , of size  {size} and shoe size  {shoe_size}')
 return recommendation
