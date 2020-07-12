def update_create(obj,test_string, create_string, update_string):
    try:
        it1 = obj.objects.get(**test_string)
        for c in update_string:
            setattr(it1,c, update_string[c])
            it1.save()
    except:
        n = obj.objects.create(**create_string)
        n.save()
        return n.id