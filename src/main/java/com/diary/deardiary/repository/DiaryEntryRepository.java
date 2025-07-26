package com.diary.deardiary.repository;

import com.diary.deardiary.model.DiaryEntry;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DiaryEntryRepository extends JpaRepository<DiaryEntry, Long> {
}
