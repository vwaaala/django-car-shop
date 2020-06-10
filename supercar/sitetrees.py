from sitetree.utils import tree, item


sitetrees = (
    tree(
        'root',
        items=[
            item('Offers', '/offers/', url_as_pattern=False, children=[in_menu=False, in_sitetree=False),
                 item('Add Offer', 'offer-add'),
                 ])
    ]),
tree('other', items=[item('Item', '/item/', url_as_pattern=False, access_guest=False)
                     ]),
