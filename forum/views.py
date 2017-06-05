from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.forms import formset_factory
from polls.models import PollSubject
from polls.forms import PollSubjectForm, PollForm
from .models import Subject, Thread, Post
from .forms import ThreadForm, PostForm


@login_required(login_url='/login/')
def forum(request):
    return render(request, 'forum-subjects.html', {'subjects': Subject.objects.all()})


@login_required(login_url='/login/')
def threads(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'threads.html', {'subject':subject})


@login_required(login_url='/login/')
def new_thread(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    poll_subject_formset = formset_factory(PollSubjectForm, extra=3)

    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)
        poll_form = PollForm(request.POST)
        poll_subject_formset = poll_subject_formset(request.POST)

        if thread_form.is_valid() and post_form.is_valid() and poll_form.is_valid() and poll_subject_formset.is_valid():
            thread = thread_form.save(False)
            thread.subject = subject
            thread.user = request.user
            thread.save()

            post = post_form.save(False)
            post.user = request.user
            post.thread = thread
            post.save()

            if request.POST.get('is_a_poll', None):

                poll = poll_form.save(False)
                poll.thread = thread
                poll.save()

                for subject_form in poll_subject_formset:
                    subject = subject_form.save(False)
                    subject.poll = poll
                    subject.save()

            messages.success(request, "You have created a new thread")

            return redirect(reverse('thread', args={thread.pk}))

    else:
        thread_form = ThreadForm()
        post_form = PostForm(request.POST)
        poll_form = PollForm()
        poll_subject_formset = poll_subject_formset()

    args = {
        'thread_form': thread_form,
        'post_form': post_form,
        'subject': subject,
        'poll_form': poll_form,
        'poll_subject_formset': poll_subject_formset,
    }

    args.update(csrf(request))

    return render(request, 'thread_form.html', args)


@login_required(login_url='/login/')
def thread_vote(request, thread_id, subject_id):
    thread = Thread.objects.get(id=thread_id)
    subject = thread.poll.votes.filter(user=request.user)

    if subject:
        messages.error(request, "You already voted on this!")
        return redirect(reverse('thread', args={thread_id}))

    subject = PollSubject.objects.get(id=subject_id)
    subject.votes.create(poll=subject.poll, user=request.user)

    messages.success(request, "We've registered your vote!")

    return redirect(reverse('thread', args={thread_id}))


@login_required(login_url='/login/')
def thread(request, thread_id):
    thread_ = get_object_or_404(Thread, pk=thread_id)
    args = {'thread': thread_}
    args.update(csrf(request))
    return render(request, 'thread.html', args)


@login_required(login_url='/login/')
def new_post(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.thread = thread
            post.user = request.user
            post.save()

            messages.success(request, "Your post has been added to the thread!")
            return redirect(reverse('thread', args={thread.pk}))
    else:
        form = PostForm()

    args = {
        'form': form,
        'form_action': reverse('new_post', args={thread.id}),
        'button_text': 'Post Comment'
    }
    args.update(csrf(request))
    return render(request, 'post_form.html', args)


@login_required(login_url='/login/')
def edit_post(request, thread_id, post_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "You have updated your thread!")
            return redirect(reverse('thread', args={thread.pk}))
    else:
        form = PostForm(instance=post)

    args = {
        'form': form,
        'form_action': reverse('edit_post', kwargs={"thread_id": thread.id, "post_id": post.id}),
        'button_text': 'Update Comment'
    }
    args.update(csrf(request))
    return render(request, 'post_form.html', args)


@login_required(login_url='/login/')
def delete_post(request, thread_id, post_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    post = get_object_or_404(Post, pk=post_id)
    print post.id
    messages.success(request, "Your post was deleted!")
    return redirect(reverse('thread', args={thread_id}))
