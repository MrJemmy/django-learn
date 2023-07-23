from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.forms.models import modelformset_factory  # model form for query sets
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm


# Create your views here.
@login_required
def recipe_list_view(request, id=None):
    qs = Recipe.objects.filter(user=request.user)
    print(qs)
    context = {
        'object_list' : qs
    }
    return render(request, 'recipes/list.html', context)

@login_required
def recipe_detail_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    context = {
        'object': obj
    }
    return render(request, 'recipes/detail.html', context)

@login_required
def recipe_create_view(request, id=None):
    form = RecipeForm(request.POST or None)
    context = {
        'modelform' : form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'recipes/create-update.html', context)

@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)  # instance=obj with help of this form get data already exist.
    # initial = {'name' : 'Please input the name'}  it is also give data we want, while inserting it throw and error.
    RecipeIngredientFormSet = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm, extra=0)
    qs = obj.recipeingredient_set.all()
    formset = RecipeIngredientFormSet(request.POST or None, queryset=qs)
    context = {
        'modelform': form,
        'modelformset': formset,
        'object': obj
    }
    if request.method == 'POST':
        print(request.POST)
    if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for child_form in formset:
            child = child_form.save(commit=False)
            child.recipe = parent
            child.save()
        context['message'] = 'Data saved.'
    return render(request, 'recipes/create-update.html', context)

@login_required
def recipe_delete_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    if request.method == 'POST':
        obj.delete()
        success_url = reverse('recipes:list')
        return redirect(success_url)
    context = {
        'object': obj
    }
    return render(request, 'recipes/delete.html', context)\

@login_required
def recipe_ingredient_delete_view(request, parent_id=None, id=None):
    obj = get_object_or_404(RecipeIngredient, recipe__id=parent_id, id=id, recipe__user=request.user)
    if request.method == 'POST':
        obj.delete()
        success_url = reverse('recipes:detail', kwargs={'id': parent_id})
        return redirect(success_url)
    context = {
        'object': obj
    }
    return render(request, 'recipes/delete.html', context)