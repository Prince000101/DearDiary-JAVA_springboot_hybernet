package com.diary.deardiary.controller;

import com.diary.deardiary.model.DiaryEntry;
import com.diary.deardiary.repository.DiaryEntryRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class DiaryController {

    private final DiaryEntryRepository repo;

    public DiaryController(DiaryEntryRepository repo) {
        this.repo = repo;
    }

    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("entries", repo.findAll());
        return "index";
    }

    @GetMapping("/new")
    public String newEntryForm(Model model) {
        model.addAttribute("entry", new DiaryEntry());
        return "form";
    }

    @PostMapping("/save")
    public String saveEntry(@ModelAttribute DiaryEntry entry) {
        repo.save(entry);
        return "redirect:/";
    }

    @GetMapping("/delete/{id}")
    public String deleteEntry(@PathVariable Long id) {
        repo.deleteById(id);
        return "redirect:/";
    }
}
