from portfolioApp.models import AppDetails,FrequentQuestion

def context_processor_data(request):
    apps=AppDetails.objects.all()
    questions=FrequentQuestion.objects.all()

    #categories=Category.objects.all()
    #all_sizes=Size.objects.all()
    #all_colors=Color.objects.all()
    #categories_with_subcategories = {}
    #for category in categories:
    #    subcategories = Sub_Category.objects.filter(categorys=category)
    #    categories_with_subcategories[category] = subcategories
    return{
        'apps':apps,
        'questions':questions
        #'categories':categories,
        #'all_sizes':all_sizes,
        #'all_colors':all_colors,
        #'categories_with_subcategories':categories_with_subcategories
    }