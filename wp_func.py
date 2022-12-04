# making a function for automated wp post format
def wp_h2(heading_text):
    """return heading two code"""
    h2_code = f'<!-- wp:heading {"level":3} --><h3>{heading_text}</h3><!-- /wp:heading -->'
    return h2_code

def wp_p(p_text):
    """return paragraph code for wp"""
    p_code = f'<!-- wp:paragraph --><p>{p_text}</p><!-- /wp:paragraph -->'
    return p_code
