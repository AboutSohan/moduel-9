import wp_func
heading_one = "Where does it come from?"

para_one = "Lorem Ipsum is simply dummied text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries."

para_two = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable."

article = wp_func.wp_h2(heading_one)+wp_func.wp_p(para_one)+wp_func.wp_p(para_two)

print(article)